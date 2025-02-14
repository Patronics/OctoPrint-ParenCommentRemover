# OctoPrint ParenCommentRemover Plugin

This is a small GCODE preprocessor that removes CNC-machine style `(paren comments)` when uploaded to octoprint.

This resolves issues with firmware that doesn't have CNC G-code Standard comments enabled,
and with firmware that excludes the contents of these comments from checksums,
as Marlin does when compiled with the #define PAREN_COMMENTS configuration option. 

## Example



## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/Patronics/OctoPrint-ParenCommentRemover/archive/master.zip

