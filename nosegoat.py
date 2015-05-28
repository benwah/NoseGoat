"""
(c) copyright 2011 - matt harrison

Licensed under PSF license
"""
import os
import sys
import random

from nose.plugins import Plugin
from nose.plugins.plugintest import run_buffered as run

GOATS = [
    r"""
   _))
  > *\     _~
  `;'\\__-' \_
     | )  _ \ \
    / / ``   w w
   w w""",
    r"""
 /\\_//\
 \(o o)/____
   \-/      \
    \ ____, /
    //    ||
   ^^     ^^""",
    r"""
        /\\//\
   _____\(oo)/
  /     --\/
  \  ____||
   ||    ||
   ^^    ^^""",
    r'''
  (_(
  /_/'_____/)
  "  |      |
     |""""""|''',
    r"""
          ,,~~--___---,
         /            .~,
   /  _,~             )
  (_-(~)   ~, ),,,(  /'
   Z6  .~`' ||     \ |
   /_,/     ||      ||
~~~~~~~~~~~~W`~~~~~~W`~~~~~~~~~"""
]


class GoatPlugin(Plugin):
    enabled = True
    name = "goat-plugin"

    def options(self, parser, env=os.environ):
        parser.add_option('', '--no-goat',
                          help='do not use the goat', 
                          action='store_true'
                          )

    def configure(self, options, conf):
        self.enabled = not options.no_goat

    def begin(self):
        sys.stderr.write("{goat}\n".format(goat=random.choice(GOATS)))

if __name__ == '__main__':
    run(plugins=[GoatPlugin()])
    
