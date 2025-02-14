# coding=utf-8
from __future__ import absolute_import

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
			if char == b'('[0]:
				inside_comment = True
				comment += bytes([char])
			elif char == b')'[0]:
				inside_comment = False
				comment += bytes([char])
			elif inside_comment:
				comment += bytes([char])
			else:
				result += bytes([char])
		# extract semicolon comments
		line = result.rstrip() + b';  ' + comment.rstrip() + b'\n'
		return line

class ParenCommentRemoverPlugin(octoprint.plugin.OctoPrintPlugin):

	def remove_all_comments(self, path, file_object, links=None, printer_profile=None, allow_overwrite=True, *args, **kwargs):
		if not octoprint.filemanager.valid_file_type(path, type="gcode"):
			return file_object

		return octoprint.filemanager.util.StreamWrapper(file_object.filename, ParenCommentRemoverStream(file_object.stream()))

	def get_update_information(self, *args, **kwargs):
		return {
			"commentremover":{
				"displayName":"Paren Comment Remover Plugin",
				"displayVersion":self._plugin_version,

				# version check: github repository
				"type":"github_release",
				"user":"Patronics",
				"repo":"OctoPrint-ParenCommentRemover",
				"current":self._plugin_version,

				# update method: pip
				"pip":"https://github.com/Patronics/OctoPrint-ParenCommentRemover/archive/{target_version}.zip"
			}
		}

__plugin_name__ = "ParenCommentRemover"
__plugin_description__ = "Removes (Paren-style G-code comments) before sending to machine"
__plugin_pythoncompat__ = ">=3,<4"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ParenCommentRemoverPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
	"octoprint.filemanager.preprocessor": __plugin_implementation__.remove_all_comments,
	"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
}
