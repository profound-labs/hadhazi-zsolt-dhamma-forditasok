all:
	pandoc \
		--output "Ácsán Kaljánó Tanításai.epub" \
		--css "../assets/stylesheets/output-epub.css" \
		title.txt \
		kalyano.md && \
	~/bin/epubcheck "Ácsán Kaljánó Tanításai.epub"
