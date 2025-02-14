# OctoPrint ParenCommentRemover Plugin

This is a small GCODE preprocessor that removes CNC-machine style `(paren comments)` when uploaded to octoprint.

This resolves issues with firmware that doesn't have CNC G-code Standard comments enabled,
and with firmware that excludes the contents of these comments from checksums,
as Marlin does when compiled with the #define PAREN_COMMENTS configuration option. 

## Example
#### Before
```gcode
G94 ( Millimeters per minute feed rate. )
G21 ( Units == Millimeters. )

G90 ( Absolute coordinates. )
G00 S15000 ( RPM spindle speed. )
G01 F20.00000 ( Feedrate. )
```
#### After
```gcode
G94;  ( Millimeters per minute feed rate. )
G21;  ( Units == Millimeters. )

G90;  ( Absolute coordinates. )
G00 S15000;  ( RPM spindle speed. )
G01 F20.00000;  ( Feedrate. )
```
## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/Patronics/OctoPrint-ParenCommentRemover/archive/master.zip

