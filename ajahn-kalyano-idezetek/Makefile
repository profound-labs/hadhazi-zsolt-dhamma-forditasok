all:
	pandoc \
		--output "Ácsán Kaljánó Idézetek.epub" \
		--css "../assets/stylesheets/output-epub.css" \
		title.txt \
		kalyano.md && \
	~/bin/epubcheck "Ácsán Kaljánó Idézetek.epub"
