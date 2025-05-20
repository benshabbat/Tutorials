const matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];
  
  function diagonalSum(matrix) {
    let sum = 0;
    const n = matrix.length;
  
    for (let i = 0; i < n; i++) {
      // הוספת האלכסון הראשי
      sum += matrix[i][i];
      // הוספת האלכסון המשני (אם זה לא אותו איבר באלכסון הראשי)
      if (i !== n - i - 1) {
        sum += matrix[i][n - i - 1];
      }
    }
  
    return sum;
  }
  
  console.log(diagonalSum(matrix)); // פלט: 25