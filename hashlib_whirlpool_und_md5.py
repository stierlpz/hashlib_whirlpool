{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "hashlib - whirlpool und md5",
      "private_outputs": true,
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyM6YKJTWtnKeqxJdBRt9bM2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/stierlpz/hashlib_whirlpool/blob/main/hashlib_whirlpool_und_md5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "V6pAvQoWy05E"
      },
      "source": [
        "import hashlib\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JK0MPIdhjIlS"
      },
      "source": [
        "h=hashlib.new('whirlpool')\n",
        "\n",
        "h.update(b\"Password\") ##<--Trage in den \" \" - Zeichen das Passwort ein!\n",
        "print(\"Hasheregebnis: \",h.hexdigest())\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xJvqEPeCIFWh",
        "collapsed": true
      },
      "source": [
        "h=hashlib.new('md5')\n",
        "\n",
        "h.update(b\"Password!\") ##<--Trage in den \" \" - Zeichen das Passwort ein!\n",
        "print(\"Hasheregebnis: \",h.hexdigest())\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}