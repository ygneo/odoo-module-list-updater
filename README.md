# odoo-module-list-updater
Allows to update Odoo 10 module list via CLI

1. Copy this repo files in your `ADDONS_PATH`, in a directory called `module-list-updater`. 

1. Manually install this module via Odoo web interface. You need to activate developer mode in settings, go to Apps > Update module list, and then look for `module-list-updater`.

Once installed, you can run odoo with `-u module-list-update` and it will update module list before starting Odoo.

See:https://www.odoo.com/forum/help-1/question/how-to-update-module-list-from-command-line-84385
