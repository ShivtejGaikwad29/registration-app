# Flask Event Registration App 🎉

This is a simple Flask web application that lets users register for an event. It features a styled registration form, a thank-you page, and is deployed on Google App Engine using the `gcloud` CLI.

---

## 🚀 Deployment on Google Cloud (App Engine)
https://cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project

Follow these steps to deploy the app on GCP:

### 1. Install and Initialize the `gcloud` CLI

If not installed yet:
👉 [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)

Then run:

```bash
gcloud init
```

### 2. Create a New GCP Project (if not done already)

```bash
gcloud projects create YOUR_PROJECT_ID
gcloud config set project YOUR_PROJECT_ID
```

### 3. Enable App Engine and Create the App

```bash
gcloud app create
```

Choose your preferred region when prompted (e.g., `us-central`).

### 4. Deploy the Flask App

```bash
gcloud app deploy
```

Once deployed, open the URL provided (something like `https://your-project-id.ew.r.appspot.com`).

### 5. View Logs (Optional)

```bash
gcloud app logs read
```

---

## 🧰 Helpful `gcloud` Commands

| Command                                     | Purpose                                             |
| ------------------------------------------- | --------------------------------------------------- |
| `gcloud init`                               | Initialize the CLI and login to your Google account |
| `gcloud config set project YOUR_PROJECT_ID` | Set active project                                  |
| `gcloud app create`                         | Create App Engine app                               |
| `gcloud app deploy`                         | Deploy your app                                     |
| `gcloud app browse`                         | Open the deployed app in a browser                  |
| `gcloud app logs read`                      | View logs                                           |
| `gcloud app services list`                  | List deployed services                              |
| `gcloud app versions list`                  | Show all versions                                   |
| `gcloud app versions delete VERSION_ID`     | Delete old versions                                 |

---

## 📂 Project Structure

```
🔽﻿
├── main.py                 # Flask application
├── app.yaml                # GCP deployment config
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css           # CSS styling
└── templates/
    ├── index.html          # Registration form
    └── thankyou.html       # Confirmation page
```

---

## 🔧 Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   python main.py
   ```

---

## 📄 License

Free to use for educational or demo purposes.
