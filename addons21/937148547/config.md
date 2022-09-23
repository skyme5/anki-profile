The default configuration of this add-on changes nothing from Anki’s defaults.

Anki can compile LaTeX to PNG or SVG files, and you can specify a different set of commands to build each. SVG files are superior because they are vectorized and scalable, but some clients do not support them yet, so you currently need to turn them on in the note type’s options if you want to use them. It’s probably best to set up the commands for generating both types of files so that you can generate the type you need at any time by changing the note type options.

For each type of build (`pngcommands` or `svgCommands`), you may insert any number of commands to be run in sequence when Anki generates a LaTeX image. Each command consists of a path to an executable program and zero or more arguments, each separated by commas. Both the entire list of commands and each command within the list is wrapped in [square brackets].

If you are having trouble configuring this add-on, you may ask on the add-ons forum.

*If you are using this add-on on Windows, you must use double backslashes (\\\\) in any paths you include: "C:\\\\Windows", not "C:\\Windows".*
