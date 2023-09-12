def find_mime_type(filename):
    # Cleanup filename
    filename = filename.lower().strip()
    mime_type = 'application/octet-stream'

    if filename.endswith('.gif'):
        mime_type = 'image/gif'
    elif filename.endswith('.jpg') or filename.endswith('.jpeg'):
        mime_type = 'image/jpeg'
    elif filename.endswith('.png'):
        mime_type = 'image/png'
    elif filename.endswith('.pdf'):
        mime_type = 'application/pdf'
    elif filename.endswith('.txt'):
        mime_type = 'text/plain'
    elif filename.endswith('.zip'):
        mime_type = 'application/zip'

    # Map extension to MIME type
    return mime_type


def main():
    # Prompt for filename
    filename = input('What is the filename? ')
    mime_type = find_mime_type(filename)
    print(f'The MIME type is {mime_type}')


main()
