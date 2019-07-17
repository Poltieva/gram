## Sublime Text

### Intro

Text editors are linguists' best friends. If you haven't befriended a text editor yet, now's the right time. A text editor is not just some space for writing texts; it's a powerful tool that allows automizing all possible text processing functions. If you succeed in this class, you will never return to manual text editing again.

There are various text editors. You all definitely know Notepad, Wordpad and MS Word / Libre Office Text Editor. These editors are not very helpful for linguists, though. Of course, you can choose the right font and text colour, but it won't help you automatically process a large amount of text data quickly. Text editors like Notepad++, Gedit, Emacs or Sublime Text that we will master today prove to be much more useful for linguists.

Sublime can be installed for Windows, Linux and OS X. It's free and very very handy.

![Why don't you use Sublime?](images/tony-stark.jpg)

### Selection

`Shift + arrows` - simple selection. Note that when you select a word, all instances of this word are highlighted.

`Ctrl + D` - select the next word and then the same words sequentially (with the ability to edit them). For OS X: `Cmd + D`.

`Ctrl + L` - select lines sequentially (with the ability to edit them). For OS X: `Cmd + L`.

`Ctrl + A` - select the whole text. For OS X: `Cmd + A`.

`Ctrl + Shift + L` / `Selection -> Split into Lines` allows modifying all lines at the same time. For OS X: `Cmd + Shift + L`.

`Shift + Drag a Right Mouse Button` - select columns. For OS X: `Option + Drag a Left Mouse Button`. Drag the mouse to the left/right and up/down. A rectangular area of text will be selected.

### Basic Editing

Sublime allows soft and hard `undo` and `redo`. The soft `undo` and `redo` account for every move (for example, highlights). `Ctrl + Z` / `Ctrl + Shift + Z` - hard `undo` and `redo`. `Ctrl + U` / `Ctrl + Shift + U` - soft `undo` and `redo`. For OS X: `Cmd + Z` / `Cmd + Shift + Z` and `Cmd + U` / `Cmd + Shift + U`.

`Tab` / `Tab + Shift` - indent / dedent text.

`Ctrl + Shift + Up/Down` - move the line up or down. For OS X: `Cmd + Ctrl + Up/Down`.

`Ctrl + Shift + D` - duplicate the line. For OS X: `Cmd + Shift + D`.

`Ctrl + Shift + K` - kill the line.

`Ctrl + K, Ctrl + K` - kill to the end of the line. For OS X: `Ctrl + K`.

`Ctrl + Shift + Backspace` - kill to the beginning of the line. For OS X: `Cmd + Del`.

`Ctrl + J` - join the next line to the current one. For OS X: `Cmd + J`.

`Ctrl + T` - transpose two characters.

### Search

`Ctrl + F` / `Find -> Find` opens a search panel. For OS X: `Cmd + F`.

Buttons:
- `Find` - go to the next substring that matches your query.
- `Find Prev` - go to the previous substring that matches your query.
- `Find All`- select all substrings that match your query (you can then copy, delete or modify them in any possible way).

Options (from right to left):
- `Highlight matches` highlights all strings that match your search query, shows the number of matches and which match you are currently on.
- `In selection` conducts search within the selected area. (NB! Reopen the search bar when you want to use it.)
- `Wrap` allows going to the last substring that matches your query and then to the very first again.
- `Whole word` adds word boundaries while searching.
- `Case sensitive` allows case-sensitive match.
- `Regular expression` allows searching using regular expressions.

`Ctrl + F3` / `Find -> Quick Find` - find all instances of the substring following the cursor. For OS X: `Cmd + Alt + G`.

`Alt + F3` / `Find -> Quick Find All` - find and highlight all instances of the word following the cursor. For OS X: `Cmd + Ctrl + G`.

### Replace

`Ctrl + H` / `Find -> Replace` opens a replace panel. For OS X: `Cmd + Alt + F`.

Buttons:
- `Replace` - replace the current matched string with a new one.
- `Replace all` - replace all matched strings in the document with a new one.

Options:
- `Preserve case` preserves the case of the matched string while replacing it with the new one.

`Ctrl + Shift + F` / `Find -> Find in files... ` opens a find/replace-in-all-files panel. For OS X: `Cmd + Shift + F`.

Buttons:
- `Where` - choose in which files to search/replace and use filters if necessary.

Options:
- `Show Context` shows the context of the lines in which the substring was found across all files. When off, only the lines with the substring are shown.
- `Use Buffer` opens a new file with the search results.

NB! The find and replace panels are resizable.

### Convert Case

`Ctrl + K, Ctrl + U` and `Ctrl + K, Ctrl + L` - transform the selected text into uppercase or lowercase. For OS X: `Cmd + K, Cmd + U` and `Cmd + K, Cmd + L`. You can also find the `Title case` and `Swap case` functions at `Edit -> Convert Case`.

### Line Permutations

`F9` / `Edit -> Sort Lines` - sort the lines in the file alphabetically. For OS X: `F5`.

`Ctrl + F9` / `Edit -> Sort Lines (Case sensitive)` - sort the lines in the file alphabetically, sorting the capitalized words first. For OS X: `Ctrl + F5`.

`Edit -> Permute Lines -> Reverse` - reverse the lines in the file.

`Edit -> Permute Lines -> Unique` - remove the duplicate lines in the file.

`Edit -> Permute Lines -> Shuffle` - shuffle the lines in the file.

The same permutations can be applied to selections.

### Goto

`Ctrl + G` - go to the line knowing its number.

`Ctrl + M` - go to the matching bracket (round, curly or square). Also, `Ctrl + Shift + M` - select text in brackets.

### Marks

With Sublime you can set a mark in the text file. The mark helps you modify large chunks of text.

`Edit -> Mark -> Set Mark` - set a mark.

`Edit -> Mark -> Clear Mark` - clear the mark.

`Edit -> Mark -> Select to Mark` - select text to the mark.

`Edit -> Mark -> Delete to Mark` - delete text to the mark.

### Macros

Macros allow recording a number of actions and then reproducing them when necessary. Sadly, the find and replace functions cannot be recorded. Use the RegReplace plugin for these. 

`Ctrl + Alt + Q` / `Tools -> Record Macro` - start or stop recording a macro. For OS X: `Ctrl + Q`.

`Ctrl + Shift + Q` / `Tools -> Playback Macro` - apply the last recorded macro.

`Tools -> Save Macro...` - save the recorded macro.

`Tools -> Macros` - the list of available macros.

### Command Palette

`Ctrl + Shift + P` - open a Command Palette. Here you can start typing the name of any command that you need. For OS X: `Cmd + Shift + P`.

### Package Control

The Sublime Text package manager that makes it exceedingly simple to find, install and keep packages up-to-date.

`Ctrl + Shift + P` - open a Command Palette. Start typing "Package Control:" here and you will see such useful commands as "Install Package", "Remove Package", "Upgrade Package", etc. For OS X: `Cmd + Shift + P`.

### Useful Plugins

#### The SublimeFileDiffs plugin

Right click on the file you want to compare, then choose `File Diffs Menu` or `Diff with Tab` that asks you to choose the second file for comparison. As a result, a new file appears, showing the lines that coincide (white lines), the lines that are present only in the second file (green lines) and the lines that are present only in the first file (red lines).

#### The Trimmer plugin

Removes unnecessary spaces and lines.

#### The SublimeREPL plugin

Runs interactive interpreters of several languages within a normal editor tab. SublimeREPL has a built-in support for command history and transferring code from open buffers to the interpreters for evaluation, enabling interactive programming.

![His coding is Sublime](images/black-mirror.png)

### Other nice things

Sublime has tabs.

Sublime saves files in the UTF-8 coding automatically.

Sublime automatically adds the closing brackets and quotation marks.

After selecting a substring, press a quotation mark or a left bracket, and Sublime will embrace the substring you selected with the punctuation the you chose.

Sublime supports yanking (`Ctrl + Y`). It pastes the text that was last killed. Yanking uses a different buffer from copy/paste.

`Ctr + Shift + T` - reopen a closed tab. For OS X: `Cmd + Shift + T`.

To close any unnecessary panel, use `Esc`.

Sublime has multiple view options: layouts, font size, colour scheme, bars, rulers, word wrap, etc.

You can create your own key bindings with Sublime.

### References

1. The Sublime Text website, available at http://www.sublimetext.com/
2. The Sublime Text unofficial documentation, available at http://sublime-text-unofficial-documentation.readthedocs.io/en/latest/
3. Some useful Sublime Text plugins described at http://www.hongkiat.com/blog/sublime-text-plugins/ and http://www.sitepoint.com/10-essential-sublime-text-plugins-full-stack-developer/
