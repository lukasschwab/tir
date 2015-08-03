import click, sys, os, datetime

def main():
    # Ask for each input with click
    url = click.prompt("URL: ")
    name = click.prompt("Title: ")
    author = click.prompt("Author: ")
    note = click.prompt("Note: ")
    today = datetime.date.today().strftime("%B %d, %Y")

    # Render into HTML
    htmlString = '<tr> <td><a href="'+url+'">'+name+'</a></td> <td>'+author+'</td> <td>'+note+'</td> <td>'+today+'</td> </tr>'
    print htmlString

    # Check if it's a new day
    # Create the new table if it is
    # Remove the date column in the table

    # Add into file
    path = "tir.html"
    f = open(path, "r")
    contents = f.readlines()
    f.close()

    contents.insert(-1, htmlString)

    f = open(path, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

    sys.exit(0)

main()