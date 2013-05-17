CONVERT=pandoc
SCLL=software-carpentry-lessons-learned

all : ${SCLL}.html

${SCLL}.html : ${SCLL}.md
	${CONVERT} < $< > $@

clean :
	@rm -f ${SCLL}.html *~
