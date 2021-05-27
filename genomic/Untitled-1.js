<head>
<link rel="stylesheet" href="css/style2.css">
<script>
    function myfunction()
    {
        var tbl=document.getElementById("myTable");
        var row=tbl.insertRow();
        var cell1=row.insertCell();
        var cell2=row.insertCell();
        var cell3=row.insertCell();
        cell1.innerHtml="sssl";
        cell2.innerHtml="sssl";
        cell3.innerHtml="sssl";


                }
</script>
<!-- <script>
    function myfunction()
    {
        var rollNOArray=new Array(1,2,3,4);
        var nameArray=new Array('x','d','r','t');
        var deptArray=new Array('x','d','r','t');
        var contribArray=new Array('x','d','r','t');

                   var tbl=document.getElementById("myTable");
        
        for (var count=0;count <rollNOArray.length;count++)
        {
            //alert ('Roll No:'+rollNOArray[count]+'nameArray[count]+'deptArray[count]+'
           // contribution:'+contribArray[count]');
            var row=tbl.insertRow();
            var cell1=row.insertCell(0);
            var cell2=row.insertCell(1);
            var cell3=row.insertCell(2);
            cell1.innerHtml=rollNOArray[count];
            cell2.innerHtml=nameArray[count];
            cell3.innerHtml=deptArray[count];
            cell4.innerHtml=contribArray[count];


        }


    }
</script>-->
</head>