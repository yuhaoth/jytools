PREFIX=$(HOME)/local/geany/
PKG_CONFIG_PATH=$(PREFIX)lib/pkgconfig 
export PKG_CONFIG_PATH
#~ ./configure --prefix=$HOME/local/geany
#~ ./configure --disable-html-docs --prefix=$HOME/local/geany

#depend on intltool
.PHONY: geany-plugins geany
all: geany-plugins

geany-plugins: geany 
	cd $@ && PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) ./autogen.sh  --prefix=$(PREFIX) \
	&& $(MAKE) && $(MAKE) install
geany:
	cd $@ && ./autogen.sh --disable-html-docs --prefix=$(PREFIX) \
        --enable-vte \
	&& $(MAKE) && $(MAKE) install

