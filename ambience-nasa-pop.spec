Name:          ambience-nasa-pop
Version:       0.8.1
Release:       8
Summary:       A serie of space-themed ambiences
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:       sailfish-version >= 3.0.0
BuildArch: noarch
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           https://github.com/fravaccaro/ambience-nasa-pop
License:       GPLv3

%description
A serie of space-themed ambiences based on poppy posters available on NASA website.

%files
%defattr(-,root,root,-)
/usr/share/ambience/*

%post
chmod 755 /usr/share/ambience/{name}
chmod 755 /usr/share/ambience/{name}/images
chmod 755 /usr/share/ambience/{name}/sounds
chmod 644 /usr/share/ambience/{name}/*.*
chmod 644 /usr/share/ambience/{name}/images/*.*
chmod 644 /usr/share/ambience/{name}/sounds/*.*
systemctl-user restart ambienced.service

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/ambience/{name}
systemctl-user restart ambienced.service
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "It's just upgrade"
systemctl-user restart ambienced.service
fi
fi

%changelog
* Fri Nov 9 2018 0.8.1
- Light ambiences for Sailfish 3.

* Tue Jun 6 2017 0.8.0
- Added ambience.

* Wed Jun 1 2016 0.7.0
- Sounds in ambience selector renamed.

* Fri Feb 26 2016 0.6.0
- Added ambiences.

* Thu Feb 25 2016 0.5.0
- First build.
