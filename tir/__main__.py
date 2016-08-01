import click, sys, os, datetime, hashlib

# Read file contents
# TODO: MAKE THIS PATH RELATIVE
path = os.path.expanduser("~/Desktop/Programming Projects/lukasschwab.github.io/tir.html")
with open(path, "r") as f:
    contents = [unicode(l, 'utf-8') for l in f.readlines()]

# Date handling
today = datetime.date.today().strftime("%B %d, %Y")

def add():
    # Ask for each input with click
    url = click.prompt("URL")
    name = click.prompt("Title")
    author = click.prompt("Author")
    note = click.prompt("Note")

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

    click.echo("You read it!")
    sys.exit(0)


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