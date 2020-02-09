{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Schedule",
      "provenance": [],
      "authorship_tag": "ABX9TyNagpcrxXIxjtiz2f85Heto",
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
        "<a href=\"https://colab.research.google.com/github/ngken0995/Book-an-appointment/blob/master/Schedule.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Dcc6CNS99feG",
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
        "id": "zOMV0IVD9mYg",
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
        "id": "NH3zRS8N9mmF",
        "colab_type": "text"
      },
      "source": [
        "Patient / Doctor Scheduler - Create a patient class and a doctor class. Have a doctor that can handle multiple patients and setup a scheduling program where a doctor can only handle 16 patients during an 8 hr work day.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aCZKyG7U9kwW",
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
        "id": "zfTTmRfr9f-n",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "class Doctor:\n",
        "  def __init__(self,name):\n",
        "    self.name = name\n",
        "    self.timeslot = {'9:00':'','9:30':'','10:00':'','10:30':'','11:00':'','11:30':'','12:00':'','12:30':'','1:00':'','1:30':'','2:00':'','2:30':'','3:00':'','3:30':'','4:30':'','5:00':''}"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZBJOtNv99gAt",
        "colab_type": "code",
        "colab": {}
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
        "    break"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}