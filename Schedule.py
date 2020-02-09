{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Schedulev2.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNmmfqauV4zww4kk+8twHt6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/ngken0995/Book-an-appointment/blob/master/Schedule.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wtS_uJGHKAEE",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Bdiq-5d0KUo-",
        "colab_type": "text"
      },
      "source": [
        "Patient / Doctor Scheduler - Create a patient class and a doctor class. Have a doctor that can handle multiple patients and setup a scheduling program where a doctor can only handle 16 patients during an 8 hr work day."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BY05rBT6SNnQ",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#Later, we can include the last name of a patient as their attribute.\n",
        "class Patient:\n",
        "  def __init__(self, first):\n",
        "    self.first = first"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tzydCZUQfpgO",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "class Doctor:\n",
        "  def __init__(self,name):\n",
        "    self.name = name\n",
        "    self.timeslot = {'9:00':'','9:30':'','10:00':'','10:30':'','11:00':'','11:30':'','12:00':'','12:30':'','1:00':'','1:30':'','2:00':'','2:30':'','3:00':'','3:30':'','4:30':'','5:00':''}\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zo4RsVQrdPpB",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AGOc1IH4KUTg",
        "colab_type": "code",
        "outputId": "e9c8b516-c9ed-4da0-bfd8-b013b300d43c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 476
        }
      },
      "source": [
        "jill = Doctor('Dr. Jill')\n",
        "ken = Doctor('Dr. Ken')\n",
        "while True:\n",
        "  d = input('Do you want to schedule an appointment with Dr. Jill or Dr. Ken?')\n",
        "  if d =='Dr. Jill':\n",
        "    d = jill\n",
        "  else:\n",
        "    d = ken\n",
        "  pfirst = input('What is your name? ')\n",
        "  time = input('what time do you want to schedule your appointment? ')\n",
        "#Later on, convert string of time to a time object\n",
        "  p = Patient(pfirst)\n",
        "  while True:\n",
        "#schedule a patient who doesn't have an appointment already. \n",
        "    if d.timeslot[time] == '' and p.first not in d.timeslot.values():\n",
        "      d.timeslot[time] = p.first\n",
        "      print(f'{p.first} is now scheduled to an appointment at {time}' )\n",
        "      break\n",
        "#patient already scheduled an appointment\n",
        "    elif p.first in d.timeslot.values():\n",
        "      for k,v in d.timeslot.items():\n",
        "        if v == p.first:\n",
        "          print(f'{v} already scheduled an appointment at {k}')\n",
        "      break\n",
        "    elif '' not in d.timeslot.values():\n",
        "#doctor's schedule is full.\n",
        "      print('All booked')\n",
        "      break\n",
        "    else:\n",
        "#patient should choose another time if the orginial choice is taken.\n",
        "      print('this date is not avaliable. We have these times open:')\n",
        "      for k,v in  d.timeslot.items():\n",
        "        if v == '':\n",
        "          print(k)\n",
        "      time = input('select another time: ')\n",
        "#Additional conition can be include later.  For example, patients should have an \n",
        "#option to book additional appointment with a reason time between the next appointment.\n",
        "  again = input('Is there another patient who want to schedule an appointment?')\n",
        "  if again != 'yes':\n",
        "    break\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Do you want to schedule an appointment with Dr. Jill or Dr. Ken?Dr.Ken\n",
            "What is your name? m\n",
            "what time do you want to schedule your appointment? 9:00\n",
            "m is now scheduled to an appointment at 9:00\n",
            "Is there another patient who want to schedule an appointment?yes\n",
            "Do you want to schedule an appointment with Dr. Jill or Dr. Ken?n\n",
            "What is your name? n\n",
            "what time do you want to schedule your appointment? 9:00\n",
            "this date is not avaliable. We have these times open:\n",
            "9:30\n",
            "10:00\n",
            "10:30\n",
            "11:00\n",
            "11:30\n",
            "12:00\n",
            "12:30\n",
            "1:00\n",
            "1:30\n",
            "2:00\n",
            "2:30\n",
            "3:00\n",
            "3:30\n",
            "4:30\n",
            "5:00\n",
            "select another time: 9:30\n",
            "n is now scheduled to an appointment at 9:30\n",
            "Is there another patient who want to schedule an appointment?no\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "25q3VIkZKmAT",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}