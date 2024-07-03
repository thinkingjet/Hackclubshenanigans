$(document).ready(function() {
  
  
    var getUrlParameter = function getUrlParameter(sParam) {
        var sPageURL = decodeURIComponent(window.location.search.substring(1)),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;

        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : sParameterName[1];
            }
        }
    };

  
    $(".calc-analysis-api").on( "click", function() { 
      
      	$('.content-area').css('display', 'none');
      	$('.loading-area').css('display', 'block');      
      
      	$(".demo-result").html('');
      	$(".err-result").html('');
      	$(".demo-result-label").html('');
      
		var arr = { 
					"ingr": $('#demoAnalysis').val().split(/\n|\r/)
				  };
      	var quantity, measure, weight, foodMatch, unit;
      	var totalCal, FAT, totalDailyFAT, FASAT, totalDailyFASAT, FATRN, CHOLE, totalDailyCHOLE, NA, totalDailyNA, CHOCDF, totalDailyCHOCDF, FIBTG, totalDailyFIBTG, SUGAR, SUGARadded, PROCNT, totalDailyPROCNT, VITD, totalDailyVITD, CA, totalDailyCA, FE, totalDailyFE, K, totalDailyK, err;
      	var html = '<div class="col-md-12"><table class="table">'+
                   '  <thead>'+
                   '    <tr>'+
                   '      <th>Qty</th>'+
                   '      <th>Unit</th>'+
                   '      <th>Food</th>'+
            	   '      <th>Calories</th>'+
            	   '	  <th>Weight</th>'+
                   '    </tr>'+
                   '  </thead>'+
                   '  <tbody></div>';
		$.ajax({
			url: 'https://api.edamam.com/api/nutrition-details?app_id=47379841&app_key=d28718060b8adfd39783ead254df7f92',          
			type: 'POST',
			data: JSON.stringify(arr),
			contentType: 'application/json',
			success: function(data) {
              
			if (typeof(data.totalNutrients.ENERC_KCAL) != "undefined") {
				totalCal = Math.round(data.totalNutrients.ENERC_KCAL.quantity);
			} else {totalCal = '0'};
			
			if (typeof(data.totalNutrients.FAT) != "undefined") {
				FAT = Math.round(data.totalNutrients.FAT.quantity*10)/10+' '+data.totalNutrients.FAT.unit;
			} else {FAT = '-'};
			if (typeof(data.totalDaily.FAT) != "undefined") {
				totalDailyFAT = Math.round(data.totalDaily.FAT.quantity)+' '+data.totalDaily.FAT.unit;
			} else {totalDailyFAT = '-'};	
			
			if (typeof(data.totalNutrients.FASAT) != "undefined") {
				FASAT = Math.round(data.totalNutrients.FASAT.quantity*10)/10+' '+data.totalNutrients.FASAT.unit;
			} else {FASAT = '-'};
			if (typeof(data.totalDaily.FASAT) != "undefined") {
				totalDailyFASAT = Math.round(data.totalDaily.FASAT.quantity)+' '+data.totalDaily.FASAT.unit;
			} else {totalDailyFASAT = '-'};	
			
			if (typeof(data.totalNutrients.FATRN) != "undefined") {
				FATRN = Math.round(data.totalNutrients.FATRN.quantity*10)/10+' '+data.totalNutrients.FATRN.unit;
			} else {FATRN = '-'};	

			if (typeof(data.totalNutrients.CHOLE) != "undefined") {
				CHOLE = Math.round(data.totalNutrients.CHOLE.quantity*10)/10+' '+data.totalNutrients.CHOLE.unit;
			} else {CHOLE = '-'};
			if (typeof(data.totalDaily.CHOLE) != "undefined") {
				totalDailyCHOLE = Math.round(data.totalDaily.CHOLE.quantity)+' '+data.totalDaily.CHOLE.unit;
			} else {totalDailyCHOLE = '-'};	

			if (typeof(data.totalNutrients.NA) != "undefined") {
				NA = Math.round(data.totalNutrients.NA.quantity*10)/10+' '+data.totalNutrients.NA.unit;
			} else {NA = '-'};
			if (typeof(data.totalDaily.NA) != "undefined") {
				totalDailyNA = Math.round(data.totalDaily.NA.quantity)+' '+data.totalDaily.NA.unit;
			} else {totalDailyNA = '-'};	

			if (typeof(data.totalNutrients.CHOCDF) != "undefined") {
				CHOCDF = Math.round(data.totalNutrients.CHOCDF.quantity*10)/10+' '+data.totalNutrients.CHOCDF.unit;
			} else {CHOCDF = '-'};
			if (typeof(data.totalDaily.CHOCDF) != "undefined") {
				totalDailyCHOCDF = Math.round(data.totalDaily.CHOCDF.quantity)+' '+data.totalDaily.CHOCDF.unit;
			} else {totalDailyCHOCDF = '-'};	

			if (typeof(data.totalNutrients.FIBTG) != "undefined") {
				FIBTG = Math.round(data.totalNutrients.FIBTG.quantity*10)/10+' '+data.totalNutrients.FIBTG.unit;
			} else {FIBTG = '-'};
			if (typeof(data.totalDaily.FIBTG) != "undefined") {
				totalDailyFIBTG = Math.round(data.totalDaily.FIBTG.quantity)+' '+data.totalDaily.FIBTG.unit;
			} else {totalDailyFIBTG = '-'};	

			if (typeof(data.totalNutrients.SUGAR) != "undefined") {
				SUGAR = Math.round(data.totalNutrients.SUGAR.quantity*10)/10+' '+data.totalNutrients.SUGAR.unit;
			} else {SUGAR = '-'};