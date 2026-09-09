
from flask import Flask, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

DATABASE = "users.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


BASE_STYLE = """
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
    }

    body {
        min-height: 100vh;
        background: linear-gradient(135deg, #071a17, #0d2b27, #06110f);
        color: #ffffff;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px;
    }

    .container {
        width: 100%;
        max-width: 430px;
    }

    .card {
        background: rgba(15, 35, 32, 0.95);
        border: 1px solid #24544c;
        border-radius: 18px;
        padding: 40px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.45);
    }

    .logo {
        width: 65px;
        height: 65px;
        margin: 0 auto 20px;
        border-radius: 50%;
        background: #19c37d;
        color: #06110f;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        font-weight: bold;
    }

    h1 {
        text-align: center;
        margin-bottom: 10px;
        font-size: 27px;
    }

    .subtitle {
        text-align: center;
        color: #9bbab4;
        margin-bottom: 30px;
        font-size: 14px;
    }

    label {
        display: block;
        margin-bottom: 8px;
        color: #cce3de;
        font-size: 14px;
    }

    input {
        width: 100%;
        padding: 13px;
        margin-bottom: 20px;
        border: 1px solid #35685f;
        border-radius: 9px;
        background: #091c19;
        color: white;
        outline: none;
        font-size: 14px;
    }

    input:focus {
        border-color: #19c37d;
    }

    button {
        width: 100%;
        padding: 13px;
        border: none;
        border-radius: 9px;
        background: #19c37d;
        color: #06110f;
        font-size: 15px;
        font-weight: bold;
        cursor: pointer;
    }

    button:hover {
        background: #27d990;
    }

    .link {
        text-align: center;
        margin-top: 22px;
        color: #9bbab4;
        font-size: 14px;
    }

    a {
        color: #19c37d;
        text-decoration: none;
        font-weight: bold;
    }

    a:hover {
        text-decoration: underline;
    }

    .security {
        margin-top: 22px;
        padding: 12px;
        background: #0b2420;
        border-radius: 9px;
        text-align: center;
        color: #9bbab4;
        font-size: 12px;
    }

    .message {
        text-align: center;
        margin-top: 15px;
        color: #19c37d;
    }
</style>
"""


@app.route("/")
def home():
    return BASE_STYLE + """
    <div class="container">
        <div class="card">
            <div class="logo">S</div>

            <h1>Secure User System</h1>

            <p class="subtitle">
                Secure authentication and user management
            </p>

            <a href="/register">
                <button>CREATE ACCOUNT</button>
            </a>

            <div style="height: 12px;"></div>

            <a href="/login">
                <button>LOGIN</button>
            </a>

            <div class="security">
                🔒 Passwords are securely hashed
            </div>
        </div>
    </div>
    """


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return BASE_STYLE + """
            <div class="container">
                <div class="card">
                    <h1>Registration</h1>
                    <p class="message">Username and password are required.</p>
                    <div class="link"><a href="/register">Go Back</a></div>
                </div>
            </div>
            """

        if len(username) > 50:
            return "Username is too long."

        if len(password) < 8:
            return BASE_STYLE + """
            <div class="container">
                <div class="card">
                    <h1>Registration</h1>
                    <p class="message">Password must be at least 8 characters.</p>
                    <div class="link"><a href="/register">Go Back</a></div>
                </div>
            </div>
            """

        password_hash = generate_password_hash(password)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        try:
            query = "INSERT INTO users (username, password) VALUES (?, ?)"
            cursor.execute(query, (username, password_hash))
            conn.commit()

        except sqlite3.IntegrityError:
            conn.close()

            return BASE_STYLE + """
            <div class="container">
                <div class="card">
                    <h1>Registration</h1>
                    <p class="message">Username already exists.</p>
                    <div class="link">
                        <a href="/register">Try Again</a>
                    </div>
                </div>
            </div>
            """

        conn.close()

        return BASE_STYLE + """
        <div class="container">
            <div class="card">
                <div class="logo">✓</div>
                <h1>Account Created</h1>
                <p class="subtitle">
                    Your account has been securely registered.
                </p>

                <a href="/login">
                    <button>CONTINUE TO LOGIN</button>
                </a>
            </div>
        </div>
        """

    return BASE_STYLE + """
    <div class="container">
        <div class="card">
            <div class="logo">S</div>

            <h1>Create Account</h1>
            <p class="subtitle">
                Register a secure user account
            </p>

            <form method="POST">
                <label>Username</label>
                <input
                    type="text"
                    name="username"
                    maxlength="50"
                    required
                    placeholder="Enter username"
                >

                <label>Password</label>
                <input
                    type="password"
                    name="password"
                    minlength="8"
                    required
                    placeholder="Minimum 8 characters"
                >

                <button type="submit">CREATE ACCOUNT</button>
            </form>

            <div class="link">
                Already have an account?
                <a href="/login">Login</a>
            </div>

            <div class="security">
                🔒 Your password is securely hashed before storage
            </div>
        </div>
    </div>
    """


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not username or not password:
            return BASE_STYLE + """
            <div class="container">
                <div class="card">
                    <h1>Login</h1>
                    <p class="message">Username and password are required.</p>
                    <div class="link"><a href="/login">Go Back</a></div>
                </div>
            </div>
            """

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):
            return BASE_STYLE + """
            <div class="container">
                <div class="card">
                    <div class="logo">✓</div>

                    <h1>Login Successful</h1>

                    <p class="subtitle">
                        Authentication completed successfully.
                    </p>

                    <div class="security">
                        🔐 Secure authentication verified
                    </div>

                    <div class="link">
                        <a href="/">Return Home</a>
                    </div>
                </div>
            </div>
            """

        return BASE_STYLE + """
        <div class="container">
            <div class="card">
                <h1>Login Failed</h1>

                <p class="subtitle">
                    Invalid username or password.
                </p>

                <a href="/login">
                    <button>TRY AGAIN</button>
                </a>
            </div>
        </div>
        """

    return BASE_STYLE + """
    <div class="container">
        <div class="card">
            <div class="logo">S</div>

            <h1>Welcome Back</h1>

            <p class="subtitle">
                Sign in to your secure account
            </p>

            <form method="POST">
                <label>Username</label>
                <input
                    type="text"
                    name="username"
                    maxlength="50"
                    required
                    placeholder="Enter username"
                >

                <label>Password</label>
                <input
                    type="password"
                    name="password"
                    minlength="8"
                    required
                    placeholder="Enter password"
                >

                <button type="submit">LOGIN</button>
            </form>

            <div class="link">
                Don't have an account?
                <a href="/register">Register</a>
            </div>

            <div class="security">
                🔒 Secure authentication enabled
            </div>
        </div>
    </div>
    """


if __name__ == "__main__":
    init_db()
    app.run(debug=False)

