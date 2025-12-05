from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import re

app = Flask(__name__)
app.secret_key = "change_this_secret_key"  # for flash messages


def run_nmap(target: str):
    """
    Runs a faster nmap service/version scan on the given target.
    """
    cmd = [
        "nmap",
        "-F",          # fast mode: fewer ports
        "-sV",         # service/version scan
        "-Pn",         # no ping (treat host as up)
        "-T4",         # faster timing template
        "--max-retries", "2"
    ]

    cmd.append(target)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=180  # increased timeout to 180 seconds
        )
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired as e:
        # custom message for timeout
        return "", f"Scan timed out after {e.timeout} seconds. Try scanning a local IP (e.g. 192.168.x.x) or use a simpler scan."
    except Exception as e:
        return "", str(e)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form.get("target", "").strip()

        if not target:
            flash("Please enter an IP address or domain.", "error")
            return redirect(url_for("index"))

        # very simple validation: only allow letters, numbers, dots, dashes, colons
        if not re.match(r"^[0-9a-zA-Z\.\-:]+$", target):
            flash("Invalid target format.", "error")
            return redirect(url_for("index"))

        stdout, stderr = run_nmap(target)

        # if completely failed
        if not stdout and stderr:
            flash("Error running nmap: " + stderr[:200], "error")
            return redirect(url_for("index"))

        return render_template("result.html", target=target, output=stdout, error=stderr)

    return render_template("index.html")


if __name__ == "__main__":
    # debug=True only for development
    app.run(debug=True)
