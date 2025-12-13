// שלב 1: פונקציות כערכים
function step1() {
    const output = document.getElementById('output1');
    
    // פונקציה רגילה
    function sayHello() {
        return "שלום!";
    }
    
    // שמירת פונקציה במשתנה
    const greeting = sayHello;
    
    // הוספת פונקציה למערך
    const functions = [sayHello, greeting];
    
    let result = `
        <h3>דוגמה 1: פונקציות כערכים</h3>
        <p><strong>קריאה רגילה:</strong> ${sayHello()}</p>
        <p><strong>קריאה דרך משתנה:</strong> ${greeting()}</p>
        <p><strong>קריאה מתוך מערך:</strong> ${functions[0]()}</p>
        <p><strong>הסבר:</strong> פונקציות ב-JS הן ערכים רגילים - אפשר לשמור אותן במשתנים, במערכים ולהעביר אותן!</p>
    `;
    
    output.innerHTML = result;
}

// שלב 2: פונקציה שמקבלת פונקציה
function step2() {
    const output = document.getElementById('output2');
    
    // HOF פשוטה - מקבלת פונקציה ומריצה אותה
    function runTwice(func) {
        func();
        func();
    }
    
    let counter = 0;
    function count() {
        counter++;
        console.log(`ספירה: ${counter}`);
    }
    
    runTwice(count);
    
    let result = `
        <h3>דוגמה 2: פונקציה שמקבלת פונקציה</h3>
        <p><strong>הפונקציה runTwice מריצה פונקציה פעמיים!</strong></p>
        <p>התוצאה: ספירה: 1, ספירה: 2</p>
        <p><strong>הסבר:</strong> runTwice היא Higher Order Function כי היא מקבלת פונקציה אחרת כפרמטר.</p>
        <pre style="background: #f4f4f4; padding: 10px; direction: ltr;">
function runTwice(func) {
    func();  // הרצה ראשונה
    func();  // הרצה שנייה
}</pre>
    `;
    
    output.innerHTML = result;
}

// שלב 3: forEach
function step3() {
    const output = document.getElementById('output3');
    
    const fruits = ['תפוח', 'בננה', 'תפוז', 'אבטיח'];
    let resultText = '';
    
    // דרך רגילה עם לולאה
    let withLoop = '<strong>עם לולאת for:</strong><br>';
    for (let i = 0; i < fruits.length; i++) {
        withLoop += `${i + 1}. ${fruits[i]}<br>`;
    }
    
    // דרך מודרנית עם forEach
    let withForEach = '<strong>עם forEach:</strong><br>';
    fruits.forEach(function(fruit, index) {
        withForEach += `${index + 1}. ${fruit}<br>`;
    });
    
    // דרך קצרה עם Arrow Function + כל הפרמטרים
    let withArrow = '<strong>עם Arrow Function:</strong><br>';
    fruits.forEach((fruit, index) => {
        withArrow += `${index + 1}. ${fruit}<br>`;
    });
    
    // הצגת כל הפרמטרים
    let allParams = '<strong>כל הפרמטרים:</strong><br>';
    fruits.forEach((element, index, array) => {
        allParams += `אינדקס ${index}: ${element} (מתוך ${array.length} פריטים)<br>`;
    });
    
    let result = `
        <h3>דוגמה 3: forEach - מעבר על מערך</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div>${withLoop}</div>
            <div>${withForEach}</div>
        </div>
        <div style="margin-top: 15px; background: #fffacd; padding: 15px; border-radius: 5px;">
            <h4>🎯 הפרמטרים שהפונקציה מקבלת:</h4>
            <pre style="background: #f4f4f4; padding: 10px; direction: ltr;">
array.forEach((element, index, array) => {
    // element - האיבר הנוכחי
    // index - המיקום במערך (0, 1, 2...)
    // array - המערך המלא (לא בשימוש תדיר)
});</pre>
            ${allParams}
        </div>
        <p><strong>הסבר:</strong> forEach היא HOF שמקבלת פונקציה ומפעילה אותה על כל איבר במערך.</p>
        <p><strong>⭐ חשוב:</strong> בדרך כלל משתמשים רק ב-element ו-index. הפרמטר השלישי (array) נדיר בשימוש.</p>
    `;
    
    output.innerHTML = result;
}

// שלב 4: map
function step4() {
    const output = document.getElementById('output4');
    
    const numbers = [1, 2, 3, 4, 5];
    
    // הכפלה ב-2
    const doubled = numbers.map(num => num * 2);
    
    // העלאה בריבוע
    const squared = numbers.map(num => num ** 2);
    
    // המרה למחרוזות
    const strings = numbers.map(num => `המספר ${num}`);
    
    // שימוש באינדקס
    const withIndex = numbers.map((num, index) => `#${index + 1}: ${num}`);
    
    // דוגמה מתקדמת - שימוש בכל הפרמטרים
    const advanced = numbers.map((element, index, array) => {
        const isLast = index === array.length - 1;
        return isLast ? `${element} (אחרון)` : element;
    });
    
    let result = `
        <h3>דוגמה 4: map - יצירת מערך חדש</h3>
        <p><strong>המערך המקורי:</strong> [${numbers.join(', ')}]</p>
        <p><strong>הכפלה ב-2:</strong> [${doubled.join(', ')}]</p>
        <p><strong>העלאה בריבוע:</strong> [${squared.join(', ')}]</p>
        <p><strong>המרה למחרוזות:</strong> [${strings.join(', ')}]</p>
        <p><strong>עם אינדקס:</strong> [${withIndex.join(', ')}]</p>
        <p><strong>דוגמה מתקדמת:</strong> [${advanced.join(', ')}]</p>
        
        <div style="margin-top: 15px; background: #e3f2fd; padding: 15px; border-radius: 5px;">
            <h4>🎯 הפרמטרים ב-map:</h4>
            <pre style="background: #f4f4f4; padding: 10px; direction: ltr;">
array.map((element, index, array) => {
    // element - האיבר הנוכחי
    // index - המיקום במערך
    // array - המערך המלא
    return newValue;  // חשוב! map חייבת להחזיר ערך
});</pre>
        </div>
        
        <p><strong>הסבר:</strong> map יוצרת מערך חדש - לא משנה את המערך המקורי!</p>
        <p><strong>⚠️ שים לב:</strong> map חייבת להחזיר ערך! הערך שמוחזר הוא מה שיהיה במערך החדש.</p>
    `;
    
    output.innerHTML = result;
}

// שלב 5: filter
function step5() {
    const output = document.getElementById('output5');
    
    const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    
    // מספרים זוגיים
    const evenNumbers = numbers.filter(num => num % 2 === 0);
    
    // מספרים גדולים מ-5
    const greaterThanFive = numbers.filter(num => num > 5);
    
    // מספרים זוגיים וגדולים מ-5
    const evenAndGreater = numbers.filter(num => num % 2 === 0 && num > 5);
    
    // שימוש באינדקס - רק איברים במיקומים זוגיים
    const evenIndexes = numbers.filter((num, index) => index % 2 === 0);
    
    // דוגמה מתקדמת - מספרים שגדולים מהממוצע
    const average = numbers.reduce((sum, num) => sum + num, 0) / numbers.length;
    const aboveAverage = numbers.filter((num, index, array) => {
        const avg = array.reduce((sum, n) => sum + n, 0) / array.length;
        return num > avg;
    });
    
    let result = `
        <h3>דוגמה 5: filter - סינון מערך</h3>
        <p><strong>המערך המקורי:</strong> [${numbers.join(', ')}]</p>
        <p><strong>רק זוגיים:</strong> [${evenNumbers.join(', ')}]</p>
        <p><strong>רק גדולים מ-5:</strong> [${greaterThanFive.join(', ')}]</p>
        <p><strong>זוגיים וגדולים מ-5:</strong> [${evenAndGreater.join(', ')}]</p>
        <p><strong>רק במיקומים זוגיים (0,2,4...):</strong> [${evenIndexes.join(', ')}]</p>
        <p><strong>גדולים מהממוצע (${average}):</strong> [${aboveAverage.join(', ')}]</p>
        
        <div style="margin-top: 15px; background: #fff3e0; padding: 15px; border-radius: 5px;">
            <h4>🎯 הפרמטרים ב-filter:</h4>
            <pre style="background: #f4f4f4; padding: 10px; direction: ltr;">
array.filter((element, index, array) => {
    // element - האיבר הנוכחי
    // index - המיקום במערך
    // array - המערך המלא
    return true;  // true = שמור, false = הסר
});</pre>
        </div>
        
        <p><strong>הסבר:</strong> filter מחזירה מערך חדש עם רק האיברים שעומדים בתנאי!</p>
        <p><strong>⚠️ שים לב:</strong> filter חייבת להחזיר true או false. true = האיבר נשאר, false = האיבר מוסר.</p>
    `;
    
    output.innerHTML = result;
}

// שלב 6: reduce
function step6() {
    const output = document.getElementById('output6');
    
    const numbers = [1, 2, 3, 4, 5];
    
    // סכום כל המספרים
    const sum = numbers.reduce((total, num) => total + num, 0);
    
    // מכפלה של כל המספרים
    const product = numbers.reduce((total, num) => total * num, 1);
    
    // מציאת המספר הגדול ביותר
    const max = numbers.reduce((maximum, num) => num > maximum ? num : maximum, numbers[0]);
    
    // בניית מחרוזת
    const sentence = numbers.reduce((text, num) => text + num + ', ', 'המספרים: ');
    
    // שימוש באינדקס - הוספת פסיק רק בין איברים
    const formatted = numbers.reduce((text, num, index) => {
        return text + num + (index < numbers.length - 1 ? ', ' : '');
    }, '');
    
    // דוגמה מתקדמת - ספירת זוגיים ואי-זוגיים
    const count = numbers.reduce((acc, num, index, array) => {
        if (num % 2 === 0) {
            acc.even++;
        } else {
            acc.odd++;
        }
        return acc;
    }, { even: 0, odd: 0 });
    
    let result = `
        <h3>דוגמה 6: reduce - צמצום לערך אחד</h3>
        <p><strong>המערך:</strong> [${numbers.join(', ')}]</p>
        <p><strong>סכום:</strong> ${sum}</p>
        <p><strong>מכפלה:</strong> ${product}</p>
        <p><strong>המספר הגדול ביותר:</strong> ${max}</p>
        <p><strong>בניית מחרוזת:</strong> ${sentence}</p>
        <p><strong>עם עיצוב נכון:</strong> ${formatted}</p>
        <p><strong>ספירה:</strong> ${count.even} זוגיים, ${count.odd} אי-זוגיים</p>
        
        <div style="margin-top: 15px; background: #f3e5f5; padding: 15px; border-radius: 5px;">
            <h4>🎯 הפרמטרים ב-reduce:</h4>
            <pre style="background: #f4f4f4; padding: 10px; direction: ltr;">
array.reduce((accumulator, element, index, array) => {
    // accumulator - הערך המצטבר (תוצאת הפעולה הקודמת)
    // element - האיבר הנוכחי
    // index - המיקום במערך
    // array - המערך המלא
    return newAccumulator;  // הערך שיועבר הלאה
}, initialValue);  // ערך התחלתי (חשוב!)</pre>
        </div>
        
        <p><strong>הסבר:</strong> reduce "מצמצמת" את המערך לערך יחיד - סכום, מכפלה, מקסימום וכו'.</p>
        <p><strong>💡 טיפ:</strong> ה-accumulator יכול להיות מספר, מחרוזת, מערך, או אפילו אובייקט!</p>
    `;
    
    output.innerHTML = result;
}

// שלב 7: שרשור (Chaining)
function step7() {
    const output = document.getElementById('output7');
    
    const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    
    // משימה: לקחת רק זוגיים, להכפיל ב-3, לחבר הכל
    
    // דרך ארוכה
    const evenNumbers = numbers.filter(num => num % 2 === 0);
    const tripled = evenNumbers.map(num => num * 3);
    const sum = tripled.reduce((total, num) => total + num, 0);
    
    // דרך קצרה - שרשור
    const result = numbers
        .filter(num => num % 2 === 0)  // [2,4,6,8,10]
        .map(num => num * 3)            // [6,12,18,24,30]
        .reduce((total, num) => total + num, 0);  // 90
    
    let resultHTML = `
        <h3>דוגמה 7: שרשור פעולות</h3>
        <p><strong>המערך המקורי:</strong> [${numbers.join(', ')}]</p>
        <p><strong>משימה:</strong> קח רק זוגיים → הכפל ב-3 → חבר הכל</p>
        <h4>דרך ארוכה (צעד צעד):</h4>
        <p>1. אחרי filter: [${evenNumbers.join(', ')}]</p>
        <p>2. אחרי map: [${tripled.join(', ')}]</p>
        <p>3. אחרי reduce: ${sum}</p>
        <h4>דרך קצרה (שרשור):</h4>
        <p>תוצאה: ${result}</p>
        <pre style="background: #f4f4f4; padding: 10px; direction: ltr;">
const result = numbers
    .filter(num => num % 2 === 0)
    .map(num => num * 3)
    .reduce((total, num) => total + num, 0);</pre>
    `;
    
    output.innerHTML = resultHTML;
}

// שלב 8: פונקציה שמחזירה פונקציה
function step8() {
    const output = document.getElementById('output8');
    
    // יוצר פונקציות מותאמות אישית
    function createMultiplier(multiplier) {
        return function(number) {
            return number * multiplier;
        };
    }
    
    // יצירת פונקציות ספציפיות
    const double = createMultiplier(2);
    const triple = createMultiplier(3);
    const quadruple = createMultiplier(4);
    
    let result = `
        <h3>דוגמה 8: פונקציה שמחזירה פונקציה</h3>
        <p><strong>יצרנו "מפעל" לפונקציות מכפילות!</strong></p>
        <p>double(5) = ${double(5)}</p>
        <p>triple(5) = ${triple(5)}</p>
        <p>quadruple(5) = ${quadruple(5)}</p>
        <p><strong>הסבר:</strong> createMultiplier היא HOF שמחזירה פונקציה חדשה!</p>
        <pre style="background: #f4f4f4; padding: 10px; direction: ltr;">
function createMultiplier(multiplier) {
    return function(number) {
        return number * multiplier;
    };
}

const double = createMultiplier(2);
double(5);  // 10</pre>
    `;
    
    output.innerHTML = result;
}

// שלב 9: דוגמה מעשית
function step9() {
    const output = document.getElementById('output9');
    
    const students = [
        { name: 'יוסי', age: 20, grade: 85 },
        { name: 'דנה', age: 22, grade: 92 },
        { name: 'רון', age: 19, grade: 78 },
        { name: 'מיכל', age: 21, grade: 95 },
        { name: 'עומר', age: 20, grade: 88 }
    ];
    
    // 1. מציאת הסטודנטים שעברו (מעל 80)
    const passedStudents = students.filter(student => student.grade >= 80);
    
    // 2. קבלת רק השמות של הסטודנטים שעברו
    const passedNames = students
        .filter(student => student.grade >= 80)
        .map(student => student.name);
    
    // 3. חישוב ממוצע הציונים
    const averageGrade = students
        .reduce((sum, student) => sum + student.grade, 0) / students.length;
    
    // 4. מציאת הסטודנט עם הציון הגבוה ביותר
    const topStudent = students.reduce((top, student) => 
        student.grade > top.grade ? student : top
    );
    
    // 5. יצירת רשימה מעוצבת
    const formattedList = students
        .filter(student => student.grade >= 80)
        .map(student => `${student.name} - ${student.grade} נקודות`)
        .join(' | ');
    
    let result = `
        <h3>דוגמה 9: עיבוד רשימת סטודנטים</h3>
        <p><strong>סטודנטים שעברו (מעל 80):</strong> ${passedStudents.length} סטודנטים</p>
        <p><strong>שמות הסטודנטים שעברו:</strong> ${passedNames.join(', ')}</p>
        <p><strong>ממוצע הכיתה:</strong> ${averageGrade.toFixed(2)}</p>
        <p><strong>הסטודנט המצטיין:</strong> ${topStudent.name} עם ${topStudent.grade} נקודות</p>
        <p><strong>רשימה מעוצבת:</strong> ${formattedList}</p>
        <pre style="background: #f4f4f4; padding: 10px; direction: ltr;">
// קבלת שמות הסטודנטים שעברו
const passedNames = students
    .filter(student => student.grade >= 80)
    .map(student => student.name);</pre>
    `;
    
    output.innerHTML = result;
}

// שלב 10: תרגילים
function step10() {
    const output = document.getElementById('output10');
    
    let result = `
        <h3>תרגילים לתרגול עצמאי</h3>
        <div style="background: #fff3cd; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <h4>תרגיל 1: עיבוד מחירים</h4>
            <p>יש לך מערך מחירים: [100, 200, 150, 300, 250]</p>
            <p>משימות:</p>
            <ul>
                <li>הוסף מע"מ 17% לכל מחיר (map)</li>
                <li>סנן רק מחירים מעל 200 (filter)</li>
                <li>חשב את סך כל המחירים (reduce)</li>
            </ul>
        </div>
        
        <div style="background: #d1ecf1; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <h4>תרגיל 2: עיבוד טקסט</h4>
            <p>יש לך מערך מילים: ['שלום', 'עולם', 'JavaScript', 'מגניב']</p>
            <p>משימות:</p>
            <ul>
                <li>המר הכל לאותיות גדולות (map)</li>
                <li>סנן רק מילים באורך יותר מ-4 תווים (filter)</li>
                <li>צור מחרוזת אחת מכל המילים (reduce או join)</li>
            </ul>
        </div>
        
        <div style="background: #d4edda; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <h4>תרגיל 3: עיבוד משתמשים</h4>
            <p>יש לך מערך משתמשים:</p>
            <pre style="direction: ltr;">[
    { name: 'אבי', age: 25, active: true },
    { name: 'בני', age: 17, active: false },
    { name: 'גלי', age: 30, active: true }
]</pre>
            <p>משימות:</p>
            <ul>
                <li>סנן רק משתמשים פעילים</li>
                <li>סנן רק משתמשים מעל גיל 18</li>
                <li>קבל מערך של רק השמות</li>
                <li>חשב גיל ממוצע</li>
            </ul>
        </div>
        
        <div style="background: #f8d7da; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <h4>תרגיל 4: בנה HOF משלך!</h4>
            <p>צור פונקציה בשם <code>processArray</code> שמקבלת:</p>
            <ul>
                <li>מערך</li>
                <li>פונקציה לעיבוד</li>
            </ul>
            <p>הפונקציה צריכה להחזיר מערך חדש עם כל האיברים מעובדים.</p>
        </div>
        
        <h4 style="color: #28a745;">💡 טיפים:</h4>
        <ul>
            <li>פתח את ה-Console (F12) כדי לראות את התוצאות</li>
            <li>נסה לכתוב את הקוד בעצמך לפני שתסתכל בפתרונות</li>
            <li>התנסה עם שרשור של מספר פעולות</li>
            <li>זכור: map = שינוי, filter = סינון, reduce = צמצום</li>
        </ul>
    `;
    
    output.innerHTML = result;
}

// הוספת הסברים נוספים
console.log(`
📚 מדריך Higher Order Functions - מוכן לשימוש!

🎯 סיכום מהיר:
1. HOF = פונקציה שמקבלת או מחזירה פונקציה
2. forEach = מעבר על כל איבר
3. map = יצירת מערך חדש (שינוי)
4. filter = יצירת מערך חדש (סינון)
5. reduce = צמצום לערך אחד
6. ניתן לשרשר פעולות!

🚀 לחץ על הכפתורים כדי לראות דוגמאות!
`);
