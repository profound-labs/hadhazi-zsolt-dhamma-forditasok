all:
	pandoc \
		--output "Dharma Idézetek.epub" \
		--css "../assets/stylesheets/output-epub.css" \
		title.txt \
		dharma.md && \
	~/bin/epubcheck "Dharma Idézetek.epub"
