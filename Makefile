SUBDIRS := doc db

.PHONY: subdirs $(SUBDIRS) clean all 

subdirs: $(SUBDIRS) 

$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

clean: $(SUBDIRS)
