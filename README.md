# st3-settings

cd "AppData\Roaming\Sublime Text 3"
git clone https://github.com/o-hayato/st3-settings.git

rename Packages Packages_org
mklink /D Packages st3-settings\Packages
