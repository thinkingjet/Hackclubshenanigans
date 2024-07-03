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

			if (typeof(data.totalNutrients.SUGARadded) != "undefined") {
				SUGARadded = Math.round(data.totalNutrients.SUGARadded.quantity*10)/10+' '+data.totalNutrients.SUGARadded.unit;
			} else {SUGARadded = '-'};

			if (typeof(data.totalNutrients.PROCNT) != "undefined") {
				PROCNT = Math.round(data.totalNutrients.PROCNT.quantity*10)/10+' '+data.totalNutrients.PROCNT.unit;
			} else {PROCNT = '-'};
			if (typeof(data.totalDaily.PROCNT) != "undefined") {
				totalDailyPROCNT = Math.round(data.totalDaily.PROCNT.quantity)+' '+data.totalDaily.PROCNT.unit;
			} else {totalDailyPROCNT = '-'};	

			if (typeof(data.totalNutrients.VITD) != "undefined") {
				VITD = Math.round(data.totalNutrients.VITD.quantity*10)/10+' '+data.totalNutrients.VITD.unit;
			} else {VITD = '-'};
			if (typeof(data.totalDaily.VITD) != "undefined") {
				totalDailyVITD = Math.round(data.totalDaily.VITD.quantity)+' '+data.totalDaily.VITD.unit;
			} else {totalDailyVITD = '-'};	

			if (typeof(data.totalNutrients.CA) != "undefined") {
				CA = Math.round(data.totalNutrients.CA.quantity*10)/10+' '+data.totalNutrients.CA.unit;
			} else {CA = '-'};
			if (typeof(data.totalDaily.CA) != "undefined") {
				totalDailyCA = Math.round(data.totalDaily.CA.quantity)+' '+data.totalDaily.CA.unit;
			} else {totalDailyCA = '-'};	

			if (typeof(data.totalNutrients.FE) != "undefined") {
				FE = Math.round(data.totalNutrients.FE.quantity*10)/10+' '+data.totalNutrients.FE.unit;
			} else {FE = '-'};
			if (typeof(data.totalDaily.FE) != "undefined") {
				totalDailyFE = Math.round(data.totalDaily.FE.quantity)+' '+data.totalDaily.FE.unit;
			} else {totalDailyFE = '-'};	
			
			if (typeof(data.totalNutrients.K) != "undefined") {
				K = Math.round(data.totalNutrients.K.quantity*10)/10+' '+data.totalNutrients.K.unit;
			} else {K = '-'};
			if (typeof(data.totalDaily.K) != "undefined") {
				totalDailyK = Math.round(data.totalDaily.K.quantity)+' '+data.totalDaily.K.unit;
			} else {totalDailyK = '-'};

			var $msg = $('<div class="col-12"></div>');
			$msg.append('<section class="performance-facts" id="performance-facts">'+
						'	<div class="performance-facts__header">'+
						'		<h1 class="performance-facts__title">Nutrition Facts</h1>'+
						'		<p><span id="lnumser">0</span> servings per container</p>'+
						'	</div>'+
						'	<table class="performance-facts__table">'+
						'		<thead>'+
						'			<tr>'+
						'				<th colspan="3" class="amps">Amount Per Serving</th>'+
						'			</tr>'+
						'		</thead>'+
						'		<tbody>'+
						'			<tr>'+
						'				<th colspan="2" id="lkcal-val-cal"><b>Calories</b></th>'+
						'				<td class="nob">'+totalCal+'</td>'+
						'			</tr>'+
						'			<tr class="thick-row">'+
						'				<td colspan="3" class="small-info"><b>% Daily Value*</b></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<th colspan="2"><b>Total Fat</b> '+FAT+'</th>'+
						'				<td><b>'+totalDailyFAT+'</b></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<td class="blank-cell"></td>'+
						'				<th>Saturated Fat '+FASAT+'</th>'+
						'				<td><b>'+totalDailyFASAT+'</b></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<td class="blank-cell"></td>'+
						'				<th>Trans Fat '+FATRN+'</th>'+
						'				<td></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<th colspan="2"><b>Cholesterol</b> '+CHOLE+'</th>'+
						'				<td><b>'+totalDailyCHOLE+'</b></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<th colspan="2"><b>Sodium</b> '+NA+'</th>'+
						'				<td><b>'+totalDailyNA+'</b></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<th colspan="2"><b>Total Carbohydrate</b> '+CHOCDF+'</th>'+
						'				<td><b>'+totalDailyCHOCDF+'</b></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<td class="blank-cell"></td>'+
						'				<th>Dietary Fiber '+FIBTG+'</th>'+
						'				<td><b>'+totalDailyFIBTG+'</b></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<td class="blank-cell"></td>'+
						'				<th>Total Sugars '+SUGAR+'</th>'+
						'				<td></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<td class="blank-cell"></td>'+
						'				<th>Includes '+SUGARadded+' Added Sugars</th>'+
						'				<td></td>'+
						'			</tr>'+	  
						'			<tr class="thick-end">'+
						'				<th colspan="2"><b>Protein</b> '+PROCNT+'</th>'+
						'				<td><b>'+totalDailyPROCNT+'</b></td>'+
						'			</tr>'+
						'		</tbody>'+
						'	</table>'+
						'	<table class="performance-facts__table--grid">'+
						'		<tbody>'+
						'			<tr>'+			  
						'				<th>Vitamin D '+VITD+'</th>'+
						'				<td><b>'+totalDailyVITD+'</b></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<th>Calcium '+CA+'</th>'+
						'				<td><b>'+totalDailyCA+'</b></td>'+
						'			</tr>'+
						'			<tr>'+
						'				<th>Iron '+FE+'</th>'+
						'				<td><b>'+totalDailyFE+'</b></td>'+			  
						'			</tr>'+
						'			<tr class="thin-end">'+
						'				<th>Potassium '+K+'</th>'+
						'				<td><b>'+totalDailyK+'</b></td>'+
						'			</tr>'+
						'		</tbody>'+
						'	</table>'+
						'	<p class="small-info" id="small-nutrition-info">*Percent Daily Values are based on a 2000 calorie diet</p>'+
						'</section>');

                if(data.ingredients != ""){
              		$.each(data.ingredients, function(i) {

                      if(typeof(data.ingredients[i].parsed) != "undefined"){
                      
                        if (typeof(data.ingredients[i].parsed[0].quantity) != "undefined") {
                            quantity = data.ingredients[i].parsed[0].quantity;
                        } else {quantity = '-'};
                        if (typeof(data.ingredients[i].parsed[0].measure) != "undefined") {
                            measure = data.ingredients[i].parsed[0].measure;
                        } else {measure = '-'};
                        if (typeof(data.ingredients[i].parsed[0].foodMatch) != "undefined") {
                            foodMatch = data.ingredients[i].parsed[0].foodMatch;
                        } else {foodMatch = '-'}; 
                      	if (typeof(data.ingredients[i].parsed[0].weight) != "undefined") {
                            weight = data.ingredients[i].parsed[0].weight;
                        } else {weight = '-'};
                      	if (typeof(data.ingredients[i].parsed[0].nutrients.ENERC_KCAL) != "undefined") {
                            cal = data.ingredients[i].parsed[0].nutrients.ENERC_KCAL.quantity;
                          	unit = data.ingredients[i].parsed[0].nutrients.ENERC_KCAL.unit;
                        } else {cal = '-'};  
                      
                        html += '<tr>'+
                                '	<th>'+quantity+'</th>'+
                                '   <th>'+measure+'</th>'+
                                '   <th>'+foodMatch+'</th>'+
                                '   <th>'+Math.round(cal*10)/10+' '+unit+'</th>'+ 
                          		'   <th>'+Math.round(weight*10)/10+' g</th>'+ 
                                '</tr>';
                      } else {
                      	err = '<span class="addition-e">We cannot calculate the nutrition for some ingredients. Please check the ingredient spelling or if you have entered a quantities for the ingredients.</span>';
                      }
                    });
                }
				$(".demo-result").append(html);
              	$(".demo-result-label").append($msg);
				$(".err-result").append(err);
              	$(".col-demo-facts").removeClass('col-demo-facts').addClass('col-demo-facts-auto');
              
              	$('.calc-analysis-api-new').css('display', 'inline-block');
				$('.loading-area').css('display', 'none');
				$('.content-area').css('display', 'inherit');              
			},
			error: function () {
              
              	err = '<span class="addition-e">We had a problem analysing this. Please check the ingredient spelling or if you have entered a quantities for the ingredients.</span>';
              	$(".err-result").append(err);

				$('.loading-area').css('display', 'none');
				$('.content-area').css('display', 'inherit');        
			}        
		});	
    });	  
  
    $('#collapse1').on('show.bs.collapse', function () {
        $('#heading1').css('display', 'none');
    })
    $('#collapse2').on('show.bs.collapse', function () {
        $('#heading2').css('display', 'none');
    })
    $('#collapse3').on('show.bs.collapse', function () {
        $('#heading3').css('display', 'none');
    })
    $('#collapse4').on('show.bs.collapse', function () {
        $('#heading4').css('display', 'none');
    })
    $('#collapse5').on('show.bs.collapse', function () {
        $('#heading5').css('display', 'none');
    })
    $('#collapse6').on('show.bs.collapse', function () {
        $('#heading6').css('display', 'none');
    })    

  
    function foodDBCall(ingrData) {
      	var cal, pro, fat, carbs, quantity, mlabel, flabel, brand, img;
		var errMsg 		= '';
		var result 		= '';

        var param = encodeURI(ingrData);
            param = param.replace("+", "%2B");
      
		$.ajax({
			url: 'https://api.edamam.com/api/food-database/parser?nutrition-type=logging&app_id=07d50733&app_key=80fcb49b500737827a9a23f7049653b9',
			type: 'GET',
          	data: param,
			//data: {ingr: ingrData},
			success: function(data) {
				console.log(data.parsed);
				if(data.hints == ""){
					result =	'<h4>Food Database</h4>'+
								'<span class="addition-e">Ooops, nothing in our database matches what you are searching for. Please try again</span>';
					$(".foodresult").append(result);
				} else if(data.hints != "") {
					result =	'<h4>Food Database</h4>'+
								'<table class="table-res-recipe">'+
								'  <thead>'+
								'    <tr>'+
								'      <th>Image</th>'+
								'      <th>Qty</th>'+
								'      <th>Unit</th>'+
								'      <th class="col-6">Food</th>'+
								'      <th>Energy</th>'+
								'      <th class="col-2">Nutrients</th>'+
								'    </tr>'+
								'  </thead>'+
								'  <tbody>';
							
						$.each(data.hints, function(i) {
							if (i > 9) {return false};
							if (typeof(data.hints[i].food.nutrients.ENERC_KCAL) != "undefined") {
								cal = '<b>'+Math.floor(data.hints[i].food.nutrients.ENERC_KCAL)+' kcal</b>';
							} else {cal = ''}
							if (typeof(data.hints[i].food.nutrients.PROCNT) != "undefined") {
								pro = 'Protein: <b class="mes">'+Math.floor(data.hints[i].food.nutrients.PROCNT)+' g</b></br>';
							} else {pro = ''}
							if (typeof(data.hints[i].food.nutrients.FAT) != "undefined") {
								fat = 'Fat: <b class="mes">'+Math.floor(data.hints[i].food.nutrients.FAT)+' g</b></br>';
							} else {fat = ''}
							if (typeof(data.hints[i].food.nutrients.CHOCDF) != "undefined") {
								carbs = 'Carbs: <b class="mes">'+Math.floor(data.hints[i].food.nutrients.CHOCDF)+' g</b></br>';
							} else {carbs = ''}

							if (typeof(data.hints[i].food.brand) != "undefined") {
								brand = data.hints[i].food.brand+' - ';
							} else {brand = ''}
							if (typeof(data.hints[i].food.label) != "undefined") {
								flabel = data.hints[i].food.label;
							} else {flabel = ''}   
							if (typeof(data.hints[i].food.image) != "undefined") {
								img = data.hints[i].food.image;
							} else {img = 'https://developer.edamam.com/images/food.png'} 							

							result += 	'<tr>'+
										'	<th><img src="'+img+'"></th>'+
										'	<th>100</th>'+
										'   <th>g</th>'+
										'   <th>'+brand+flabel+'</th>'+
										'   <th>'+cal+'</th>'+
										'   <th class="last">'+pro+fat+carbs+'</th>'+           
										'</tr>';                        

						});
					
						result +=	'	</tbody>'+
									'</table>';
						$(".foodresult").append(result);
						
				}
				$('.loading-area').css('display', 'none');
				$('.result-area').css('display', 'block');
			}
		});	
    }  
  