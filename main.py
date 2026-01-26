from flask import send_from_directory

from __init__ import create_app

app = create_app()


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(
        app.static_folder, filename, cache_timeout=31536000
    )  # Cache for 1 year


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7704, debug=True)
