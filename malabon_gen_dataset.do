use covid_malabon.dta, clear

drop new_deaths moveave_deaths new_recovered moveave_recovered active_cases ///
new_cases moveave

append using covid_malabon_june9.dta

sort barangay date

gen active_cases = confirmed_cases - recovered - deaths
by barangay: gen new_cases = confirmed_cases[_n] - confirmed_cases[_n-1]
by barangay: gen moveave = (new_cases[_n] + new_cases[_n-1] + new_cases[_n-2] + ///
new_cases[_n-3] + new_cases[_n-4] + new_cases[_n-5] + new_cases[_n-6])/7 

by barangay: gen new_deaths = deaths[_n] - deaths[_n-1]
by barangay: gen moveave_deaths = (new_deaths[_n] + new_deaths[_n-1] + new_deaths[_n-2] + ///
new_deaths[_n-3] + new_deaths[_n-4] + new_deaths[_n-5] + new_deaths[_n-6])/7 

by barangay: gen new_recovered = recovered[_n] - recovered[_n-1]
by barangay: gen moveave_recovered = (new_recovered[_n] + new_recovered[_n-1] + new_recovered[_n-2] + ///
new_recovered[_n-3] + new_recovered[_n-4] + new_recovered[_n-5] + new_recovered[_n-6])/7 

export delimited using covid_malaboncity.csv if brgy=="Malabon City" & date>=22006, replace
export delimited using covid_malabon_map_june9.csv if brgy!="Malabon City" & date==22075, replace
export delimited using covid_malabon_all.csv, replace
