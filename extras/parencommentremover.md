---
layout: plugin

id: parencommentremover
title: ParenCommentRemover
description: Splits multiple commands on one line in GCODE files into multiple lines
author: Patrick Leiser
license: AGPLv3

date: 2025-02-11

homepage: https://github.com/Patronics/OctoPrint-ParenCommentRemover
source: https://github.com/Patronics/OctoPrint-ParenCommentRemover
archive: https://github.com/Patronics/OctoPrint-ParenCommentRemover/archive/master.zip

follow_dependency_links: false

tags:
- gcode
- preprocessing
- comments

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.0
---

This is a small GCODE preprocessor that removes CNC-machine style `(paren comments)` before sending them to your machine.

This resolves issues with firmware that doesn't have CNC G-code Standard comments enabled,
and with firmware that excludes the contents of these comments from checksums,
as Marlin does when compiled with the #define PAREN_COMMENTS configuration option

## Example

