// closure = A function defined inside of another function, 
//                  the inner function has access to the variables 
//                  and scope of the outer function.
//                  Allow for private variables and state maintenance
//                  Used frequently in JS frameworks: React, Vue, Angular

// ---------- EXAMPLE 1 ----------

function outer(){

    const message = "Hello";

    function inner(){
        console.log(message);
    }

    inner();
}

message = "Goodbye";

outer();

