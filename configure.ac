AC_PREREQ([2.57])

AC_INIT(libXxf86dga, 1.0.0, [xorg@lists.freedesktop.org], libXxf86dga)
AM_INIT_AUTOMAKE([foreign dist-bzip2])
AM_MAINTAINER_MODE

AM_CONFIG_HEADER(src/config.h)

# Check for progs
AC_PROG_CC
AC_PROG_LIBTOOL

# Checks for pkg-config packages
PKG_CHECK_MODULES(XXF86DGA, xproto x11 xextproto xext xf86dgaproto)

AC_OUTPUT([Makefile
	   src/Makefile
	   man/Makefile
	   xxf86dga.pc])
