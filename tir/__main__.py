import click, sys, os, datetime, hashlib
from xml.etree import ElementTree as ET

# NOTE: change this to your html location
html = "/Users/lukas/Desktop/Programming Projects/lukasschwab.github.io/tir.html"
feed = "/Users/lukas/Desktop/Programming Projects/lukasschwab.github.io/tir.xml"

tree = ET.parse(feed)
channel = tree.getroot()[0]

# Read file contents
path = os.path.expanduser(html)
with open(path, "r") as f:
    contents = [unicode(l, 'utf-8') for l in f.readlines()]

# Date handling
today = datetime.date.today().strftime("%B %d, %Y")
pd = datetime.date.today().strftime("%a, %d %b %Y %H:%M:%S %z")

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
    # If it's a new day, interrupt table wiht a heading
    if today != contents[0][4:-4]:
        contents[0] = "<!--"+today+"-->\n"
        # Create a new separator row
        contents.insert(-1, '\n\t<td colspan="4"><h3 id="'+hashlib.md5(today).hexdigest()+'">'+today+"</h3></td>\n")
    # Add new entry
    contents.insert(-1, htmlString)
    write(contents)

def xml(url, name, author, note):
    e = ET.SubElement(channel, "item")
    ET.SubElement(e, "title").text = name
    ET.SubElement(e, "description").text = note
    ET.SubElement(e, "pubDate").text = pd
    ET.SubElement(e, "link").text = url
    ET.SubElement(e, "guid").text = url
    ET.SubElement(e, "category").text = "tir"
    tree.write(feed)

def rm():
    # delete last post
    print "Following entry removed: \n" + contents[-2].replace("\t", "")
    del contents[-2]
    write(contents)


def write(contents):
    # Save changes to file
    with open(path, "w") as f:
        contents = "".join(contents).encode('utf-8')
        f.write(contents)


@click.command()
@click.option("--delete", is_flag=True, help="Deletes last entry")
def main(delete):
    """Parses command-line arguments for tir"""
    if delete:
        rm()
    else:
        add()

if __name__ == '__main__':
    main()