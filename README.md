# Setup before running the agent examples in this code

This guide provides step-by-step instructions for setting up your Google Cloud Platform (GCP) environment to use the Google Application Development Kit (ADK) with Vertex AI.

## Prerequisites

* A Google Account.
* Access to Google Cloud Platform ([console.cloud.google.com](https://console.cloud.google.com/)).
* Python and `pip` installed on your local system (if not using Google Cloud Shell).

## Setup Instructions

Follow these steps to configure your environment:

1.  **Create a Billing Account:**
    * Navigate to the Billing section in the Google Cloud Console.
    * If you don't have one, create a new billing account. Ensure you have valid payment information associated with it.
    * [Go to Cloud Billing Console](https://console.cloud.google.com/billing)

2.  **Create a Google Cloud Project:**
    * Create a new project within the Google Cloud Console.
    * **Crucially, link this new project to the billing account you created or confirmed in the previous step.** Projects require an active billing account to use most GCP services, including Vertex AI.
    * Note down your **Project ID**. You'll need it later.
    * [Go to Create Project](https://console.cloud.google.com/projectcreate)

3.  **Install Google Cloud CLI (`gcloud`):**
    * If you are working on your local machine (not Google Cloud Shell), you need to install the Google Cloud Command Line Interface (CLI).
    * Follow the official installation instructions for your operating system.
    * **Note:** If you are using Google Cloud Shell directly within the GCP console, `gcloud` is pre-installed, and you can skip this step.
    * [Install gcloud CLI](https://cloud.google.com/sdk/docs/install)

4.  **Configure `gcloud` Project:**
    * Check if your `gcloud` CLI is configured to use the project you just created:
        ```bash
        gcloud config list
        ```
    * Look for the `project = [YOUR_PROJECT_ID]` line in the output.
    * If it's not set or set to a different project, configure it using your specific Project ID:
        ```bash
        gcloud config set project your-google-cloud-project-id
        ```
        (Replace `your-google-cloud-project-id` with the actual ID of the project you created in Step 2).

5.  **Authenticate (Local Machine Only):**
    * If you are running `gcloud` commands from your local machine (not Cloud Shell), you need to authenticate to grant the CLI access to your Google Cloud resources. Use Application Default Credentials (ADC):
        ```bash
        gcloud auth application-default login
        ```
    * This command will open a browser window for you to log in with your Google Account and authorize access.
    * **Note:** This step is usually not required in Cloud Shell, as it's already authenticated.

6.  **Enable Vertex AI API:**
    * Before using Vertex AI services, you must enable the API for your project. You can do this via the `gcloud` command:
        ```bash
        gcloud services enable aiplatform.googleapis.com
        ```
    * Alternatively, you can enable it through the Google Cloud Console UI by searching for "Vertex AI API" in the API Library and clicking "Enable".
    * [Go to Vertex AI API page](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com)

7.  **Install Google Application Development Kit (ADK):**
    * Install the ADK library using pip:
        ```bash
        pip install google-adk
        ```
