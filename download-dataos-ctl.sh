#!/bin/bash

##############################################################################
# Copyright TMDC 2022
##############################################################################

# Downloader for dataos-ctl
#
# You can fetch the the dataos-ctl file using:
# export PRIME_APIKEY=APIKEY
# curl --silent --output download-dataos-ctl.sh --location --request GET "https://prime.tmdata.io/plutus/api/v1/files/download?name=download-dataos-ctl.sh&dir=cli-dev&apikey=$PRIME_APIKEY"
# chmod u+x download-dataos-ctl.sh
# ./download-dataos-ctl.sh
#

if [ "x${PRIME_APIKEY}" = "x" ] ; then
  printf "Need to set the env variable PRIME_APIKEY."
  exit 1;
fi

# Determine the operating system.
OS="$(uname)"
if [ "x${OS}" = "xDarwin" ] ; then
  OSEXT="darwin"
else
  OSEXT="linux"
fi

# Determine the architecture.
ARCH="$(uname -p)"
if [ "x${ARCH}" = "xamd64" ] ; then
  ARCHEXT="amd64"
fi
if [ "x${ARCH}" = "xx86_64" ] ; then
  ARCHEXT="amd64"
fi
if [ "x${ARCH}" = "xarm" ] ; then
  ARCHEXT="arm"
fi
if [ "x${ARCH}" = "xarm64" ] ; then
  ARCHEXT="arm64"
fi
if [ "x${OSEXT}" = "xdarwin" ] ; then
   ARCHEXT="amd64"
fi
# This is very specific to handle m1 apple chip. In m1 we are getting ARCH as arm instead of arm64
if [ "x${OSEXT}" = "xdarwin" ] && [ "x${ARCH}" = "xarm" ] ; then
   ARCHEXT="arm64"
fi

if [ "x${ARCHEXT}" = "x" ] ; then
  printf "Unable to determine arch. Cannot proceed, please download the file manually."
  exit 1;
fi

# Downloads the dataos-ctl binary archive.
tmp=$(mktemp -d /tmp/dataos-ctl.XXXXXX)
filename="dataos-ctl-${OSEXT}-${ARCHEXT}.tar.gz"
cd "$tmp" || exit
URL="https://prime.tmdata.io/plutus/api/v1/files/download?dir=cli-dev&name=${filename}"
printf "Downloading %s from %s ... \n" "${filename}" "${URL}"
curl --output ${filename} --location --request GET "${URL}&apikey=${PRIME_APIKEY}"
curl --output ${filename}.sha256sum --location --request GET "${URL}.sha256sum&apikey=${PRIME_APIKEY}"
printf "%s download complete!\n" "${filename}"

printf "Checksum "
shasum -a 256 -c ${filename}.sha256sum
if [ "x$?" != "x0" ] ; then
  printf "Checksum failed cannot proceed."
  exit 1;
fi

# setup dataos-ctl
tar -xzf "${filename}"
cd "$HOME" || exit
mkdir -p ".dataos/bin"
mv "${tmp}/${OSEXT}-${ARCHEXT}/dataos-ctl" ".dataos/bin/dataos-ctl"
chmod +x ".dataos/bin/dataos-ctl"
rm -r "${tmp}"

# Print message
printf "\n"
printf "Add the dataos-ctl to your path with:"
printf "\n"
printf "export PATH=\$PATH:\$HOME/.dataos/bin \n"
printf "\n"
