import click, sys, os, datetime

def main():
    # Ask for each input with click
    url = click.prompt("URL")
    name = click.prompt("Title")
    author = click.prompt("Author")
    note = click.prompt("Note")

    # Date handling
    today = datetime.date.today().strftime("%B %d, %Y")

    # Render into HTML
    htmlString = '\t<tr> <td><a href="'+url+'">'+name+'</a></td> <td>'+author+'</td> <td>'+note+'</td> <td>'+today+'</td> </tr>\n'

    # Read file contents
    # TODO: MAKE THIS PATH RELATIVE
    path = os.path.expanduser("~/Desktop/Programming Projects/tir/tir.html")
    f = open(path, "r")
    contents = f.readlines()
    f.close()

    if today != contents[0][4:-4]:
        contents[0] = "<!--"+today+"-->\n"
        # Create a new table
        contents += ['\n<h3>'+today+'</h3>\n','<table class="table">\n','\t<tr>\n','\t\t<th>Title</th>\n','\t\t<th>Author</th>\n','\t\t<th>Note</th>\n','\t\t<th>Date</th>\n','\t</tr>\n','</table>']

    # Add new entry
    contents.insert(-1, htmlString)

    # Save changes to file
    f = open(path, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

    click.echo("You read it!")
    sys.exit(0)

if __name__ == '__main__':
    main()