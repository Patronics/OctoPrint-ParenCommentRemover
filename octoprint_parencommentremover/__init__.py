# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import octoprint
import octoprint.plugin

class ParenCommentRemoverStream(octoprint.filemanager.util.LineProcessorStream):
	def process_line(self, line):
		if b'(' not in line:
			# no paren comments, bail
			return line

		comment = b''
		# extract paren comments
		inside_comment = False
		result = b''
		for char in line:
			if char == b'(':
				inside_comment = True
				comment += char
			elif char == b')':
				inside_comment = False
				comment += char
			elif inside_comment:
				comment += char
			else:
				result += char
		# extract semicolon comments
		line = result + b';' + comment.rstrip() + b'\n'
		return line

class ParenCommentRemoverPlugin(octoprint.plugin.OctoPrintPlugin):

	def remove_all_comments(self, path, file_object, links=None, printer_profile=None, allow_overwrite=True, *args, **kwargs):
		if not octoprint.filemanager.valid_file_type(path, type="gcode"):
			return file_object

		return octoprint.filemanager.util.StreamWrapper(file_object.filename, ParenCommentRemoverStream(file_object.stream()))

	def get_update_information(self, *args, **kwargs):
		return dict(
			commentremover=dict(
				displayName="Paren Comment Remover Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="Patronics",
				repo="OctoPrint-ParenCommentRemover",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/Patronics/OctoPrint-ParenCommentRemover/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "ParenCommentRemover"
__plugin_description__ = "Splits multiple commands on one GCODE line with \":\" separator into multiple lines."
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = ParenCommentRemoverPlugin()
__plugin_hooks__ = {
	"octoprint.filemanager.preprocessor": __plugin_implementation__.split_all_commands,
	"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
}
