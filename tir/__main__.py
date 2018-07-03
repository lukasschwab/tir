import click, sys, os, hashlib, pytz, webbrowser
from xml.etree import ElementTree as ET
from datetime import datetime
from dateutil import parser

# FIXME: change this to your html location
script_dir = os.path.dirname(os.path.realpath(__file__))
html = os.path.join(script_dir, "../index.html")
feed = os.path.join(script_dir, "../tir.xml")
# True -> latest additions at the bottom
INORDER = False

tree = ET.parse(feed)
channel = tree.getroot()[0]

# Read file contents
path = os.path.expanduser(html)
with open(path, "r") as f:
    contents = [unicode(l, 'utf-8') for l in f.readlines()]

# Date handling
today = datetime.today().strftime("%B %d, %Y")
pd = datetime.today().strftime("%a, %d %b %Y %H:%M:%S %z")

def add():
    # Ask for each input with click
    url = click.prompt("URL")
    name = click.prompt("Title")
    author = click.prompt("Author")
    note = click.prompt("Note")
    html(url, name, author, note)
    xml(url, name, author, note)
    click.echo("You read it!")

def html(url, name, author, note):
    # Render into HTML
    htmlString = '\t<tr> <td><a href="'+url+'">'+name+'</a></td> <td>'+author+'</td> <td>'+note+'</td> <td>'+today+'</td> </tr>\n'
    if INORDER:
        # If it's a new day, interrupt table wiht a heading
        if today != contents[0][4:-4]:
            contents[0] = "<!--"+today+"-->\n"
            # Create a new separator row
            contents.insert(-1, '\n\t<td colspan="4"><h3 id="'+hashlib.md5(today).hexdigest()+'">'+today+"</h3></td>\n")
        # Add new entry
        contents.insert(-1, htmlString)
    else: # Put it at the beginning
        if today != contents[0][4:-4]:
            pos = contents.index('\t</tr>\n') + 1
            contents.insert(pos, htmlString)
            contents[0] = "<!--"+today+"-->\n"
            contents.insert(pos, '\n\t<td colspan="4"><h3 id="'+hashlib.md5(today).hexdigest()+'">'+today+"</h3></td>\n")
        else:
            for i, s in enumerate(contents):
                if today in s and i > 0:
                    pos = i+1
                    contents.insert(pos, htmlString)
                    break
    write(contents)

def xml(url, name, author, note):
    updateFeed()
    addFeedItem(url, name, author, note)
    tree.write(feed)

def updateFeed(time=pd):
    channel.find('pubDate').text = time
    channel.find('lastBuildDate').text = pd

def addFeedItem(url, name, author, note):
    e = ET.SubElement(channel, "item")
    ET.SubElement(e, "title").text = name
    ET.SubElement(e, "description").text = note
    ET.SubElement(e, "pubDate").text = pd
    ET.SubElement(e, "link").text = url
    ET.SubElement(e, "guid").text = url
    ET.SubElement(e, "category").text = "tir"

def rm():
    if INORDER:
        # delete last post
        print "Following entry removed: \n" + contents[-2].replace("\t", "")
        del contents[-2]
        write(contents)
        rmXml()
    else:
        click.echo("Reverse-order tir doesn't support deletion.")

def rmXml():
    lastUpdated = channel.find('pubDate').text
    items = channel.findall('item')
    length = len(items)
    lastPublished = pytz.utc.localize(datetime(1, 1, 1))
    for item in items:
        pubDateText = item.find('pubDate').text
        pubDateTime = parser.parse(pubDateText)
        if pubDateText == lastUpdated:
            channel.remove(item)
        elif pubDateTime > lastPublished:
            lastPublished = pubDateTime
    if length > 1:
        # Would love to format this correctly, but probably nbd.
        updateFeed(lastPublished.strftime("%a, %d %b %Y %H:%M:%S %z"))
    else:
        updateFeed()
    tree.write(feed)

def write(contents):
    # Save changes to file
    with open(path, "w") as f:
        contents = "".join(contents).encode('utf-8')
        f.write(contents)

@click.command()
@click.option("--delete", is_flag=True, help="Deletes last entry")
@click.option("--openFile", "-o", is_flag=True, help="Opens the tir page without operation")
def main(delete, openfile):
    """Parses command-line arguments for tir"""
    if openfile:
        print "Opening " + path
        webbrowser.open("file://" + path, new=0, autoraise=True)
        return
    if delete:
        rm()
    else:
        add()

if __name__ == '__main__':
    main()
