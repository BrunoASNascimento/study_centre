#TODO: Finish the README.md file

# Advanced Analytics with PySpark

This guide provides step-by-step instructions for setting up PySpark on both Mac OS M1 and Ubuntu systems. By following these steps, you'll have a working environment for developing and running PySpark applications.

---

## Table of Contents

- [Mac OS M1 Installation](#mac-os-m1-installation)
  - [Create a Conda Environment](#create-a-conda-environment)
  - [Install Java](#install-java)
  - [Install PySpark](#install-pyspark)
  - [Install Jupyter Notebook (Optional)](#install-jupyter-notebook-optional)
- [Ubuntu Installation](#ubuntu-installation)
  - [Update and Upgrade the System](#update-and-upgrade-the-system)
  - [Install Java](#install-java-1)
  - [Install Miniconda](#install-miniconda)
  - [Create a Conda Environment](#create-a-conda-environment-1)
  - [Install PySpark](#install-pyspark-1)
  - [Install Jupyter Notebook (Optional)](#install-jupyter-notebook-optional-1)
- [Verifying the Installation](#verifying-the-installation)
- [Additional Resources](#additional-resources)

---

## Mac OS M1 Installation

### Create a Conda Environment

First, create a new Conda environment named `pyspark_env` with Python 3.9:

```bash
conda create -n pyspark_env python=3.9
```

Activate the newly created environment:

```bash
conda activate pyspark_env
```

> **Note:** Using a separate Conda environment helps isolate your PySpark installation and its dependencies from other projects.

### Install Java

PySpark requires Java to function. Install OpenJDK using Conda:

```bash
conda install -c conda-forge openjdk
```

> **Explanation:** The `conda-forge` channel provides up-to-date packages, and OpenJDK is the open-source implementation of the Java Platform.

### Install PySpark

Install PySpark from the `conda-forge` channel:

```bash
conda install -c conda-forge pyspark
```

> **Explanation:** This command installs PySpark and all its dependencies within your Conda environment.

### Install Jupyter Notebook (Optional)

If you plan to use Jupyter Notebook for your development:

```bash
conda install -c conda-forge notebook
```

Alternatively, install JupyterLab for an enhanced interface:

```bash
conda install -c conda-forge jupyterlab
```

---

## Ubuntu Installation

### Update and Upgrade the System

Before installing new packages, update the package lists and upgrade existing packages:

```bash
sudo apt update
sudo apt upgrade -y
```

> **Explanation:** Keeping your system updated ensures you have the latest security patches and software versions.

### Install Java

Install OpenJDK 11:

```bash
sudo apt install -y openjdk-11-jdk
```

Verify the installation:

```bash
java -version
```

> **Expected Output:**
>
> ```
> openjdk version "11.0.X" 2021-XX-XX
> OpenJDK Runtime Environment (build 11.0.X+XX-Ubuntu-...)
> OpenJDK 64-Bit Server VM (build 11.0.X+XX-Ubuntu-..., mixed mode)
> ```

### Install Miniconda

Download the latest Miniconda installer script:

```bash
sudo wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /opt/miniconda-installer.sh
```

Run the installer:

```bash
bash /opt/miniconda-installer.sh
```

During the installation, you'll be prompted:

```
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[no] >>>
```

Type `yes`, then press **ENTER**.

> **Note:** Initializing Miniconda modifies your shell configuration to recognize Conda commands.

After the installation, refresh your shell:

```bash
source ~/.bashrc
```

### Create a Conda Environment

Create a new Conda environment named `pyspark_env` with Python 3.9:

```bash
conda create -n pyspark_env python=3.9
```

Activate the environment:

```bash
conda activate pyspark_env
```

### Install PySpark

Install PySpark using `pip` within your Conda environment:

```bash
pip install pyspark
```

> **Explanation:** `pip` installs the latest version of PySpark compatible with your Python version.

### Install Jupyter Notebook (Optional)

If you plan to use Jupyter Notebook:

```bash
pip install notebook
```

Alternatively, install JupyterLab:

```bash
pip install jupyterlab
```

---

## Verifying the Installation

To confirm that PySpark is installed correctly, start the PySpark shell:

```bash
pyspark
```

You should see the PySpark welcome message without any errors.

Alternatively, test PySpark in a Jupyter Notebook:

1. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. Run:

   [00_test_pyspark.ipynb](00_test_spark_instalation.ipynb)

3. You should see a table displaying the data.

---

## Additional Resources

- **PySpark Documentation:** [https://spark.apache.org/docs/latest/api/python/](https://spark.apache.org/docs/latest/api/python/)
- **Conda Documentation:** [https://docs.conda.io/en/latest/](https://docs.conda.io/en/latest/)
- **Jupyter Notebook Documentation:** [https://jupyter-notebook.readthedocs.io/en/stable/](https://jupyter-notebook.readthedocs.io/en/stable/)

---
