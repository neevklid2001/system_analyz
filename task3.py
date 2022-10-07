{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/RvNbDpQ+jGYlGQtV1bvS",
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
        "<a href=\"https://colab.research.google.com/github/neevklid2001/system_analyz/blob/main/task3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "68P9jNZqwvMX"
      },
      "outputs": [],
      "source": [
        "import csv"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "with open('graf2.csv', 'r', newline='') as csvfile:\n",
        "  l=list(csv.reader(csvfile, delimiter=','))\n",
        "  "
      ],
      "metadata": {
        "id": "53sKXiO2x3e7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "r1=[]\n",
        "for item in l:\n",
        "  r1.append(item)\n",
        "r2=[]\n",
        "for item in l:\n",
        "  el=[]\n",
        "  el.append(item[1])\n",
        "  el.append(item[0])\n",
        "  r2.append(el)"
      ],
      "metadata": {
        "id": "Bv9E-kbNzL_A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "r1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aTAblVs40iKT",
        "outputId": "9decc79f-f03e-45ca-9688-10f0f3b6eba0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['1', '2'], ['1', '3'], ['2', '4']]"
            ]
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "r2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E1rt8OoH0lS8",
        "outputId": "bec9e669-e32d-4127-91db-887ec7128df7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['2', '1'], ['3', '1'], ['4', '2']]"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "r3=[]\n",
        "r4=[]\n",
        "r5=[]\n",
        "for item in r1:\n",
        "  for elem in r1:\n",
        "    if item[1]==elem[0]:\n",
        "      el=[]\n",
        "      el.append(item[0])\n",
        "      el.append(elem[1])\n",
        "      r3.append(el)\n",
        "    if (item[0]==elem[0])and(item[1]!=elem[1]):\n",
        "      el=[]\n",
        "      el.append(item[1])\n",
        "      el.append(elem[1])\n",
        "      r5.append(el)\n",
        "for item in r3:\n",
        "  el=[]\n",
        "  el.append(item[1])\n",
        "  el.append(item[0])\n",
        "  r4.append(el)"
      ],
      "metadata": {
        "id": "IUgvpwK822IR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "r3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "libqMbxw3UBy",
        "outputId": "35034d77-2334-49a2-d110-34fbdc3502a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['1', '4']]"
            ]
          },
          "metadata": {},
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "r4"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LvEIGqSP32fs",
        "outputId": "68758bc5-cd53-4fd3-9445-771cf5719ea2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['4', '1']]"
            ]
          },
          "metadata": {},
          "execution_count": 58
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "r5\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "37M-ZGHP36Xo",
        "outputId": "081a8ee2-3743-4807-b875-ba496b71ae97"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[['2', '3'], ['3', '2']]"
            ]
          },
          "metadata": {},
          "execution_count": 59
        }
      ]
    }
  ]
}