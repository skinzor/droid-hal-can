# These and other macros are documented in dhd/droid-hal-device.inc
%define device can
%define vendor Huawei

%define vendor_pretty Huawei
%define device_pretty Nova

%define installable_zip 1

%define droid_target_aarch64 1

%define straggler_files \
/init.class_main.sh\
/init.mac.sh\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
