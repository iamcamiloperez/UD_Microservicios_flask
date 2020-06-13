Feature: FlaskMocroS

Scenario Outline: Post add
  Given a <values> to add
  When the add the values
  Then the <total> of add is correct

  Examples: values
  | values         | total |
  | 5,7,6,4        | 22    |
  | 10,2,14        | 26    |
  | 15,33,2        | 50    |
  | 35,9,10        | 54    |
  | 9,10,5         | 24    |
  | 11,21,52,3     | 87    |

  Scenario Outline: Post subtract
  Given a <values> to subtract
  When the subtract the values
  Then the <total> of subtract is correct

  Examples: values
  | values         | total |
  | 50,10,2        | 38    |
  | 12,6           | 6     |
  | 33,2,1         | 30    |
  | 29,20,8        | 1     |
  | 5,1            | 4     |
  | 15,3,10        | 2     |

  Scenario Outline: Post multiply
  Given a <values> to multiply
  When the multiply the values
  Then the <total> of multiply is correct

  Examples: values
  | values         | total |
  | 50,1           | 50    |
  | 12,6           | 72    |
  | 33,2,1         | 66    |
  | 29,2           | 58    |
  | 5,1            | 5     |
  | 15,3,10        | 450   |

  Scenario Outline: Post divide
  Given a <values> to divide
  When the divide the values
  Then the <total> of divide is correct

  Examples: values
  | values         | total |
  | 50,10          | 5     |
  | 12,6           | 2     |
  | 30,2,1         | 15    |
  | 20,20          | 1     |
  | 5,1            | 5     |
  | 20,2,10        | 1     |