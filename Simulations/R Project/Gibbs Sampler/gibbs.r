GibbsSamplerFromMNormal<-function (n, r, xmean = 0, ymean = 0, stdev = 1, burnin = FALSE) 
{		
		# Determine if it is using burn in, if so get a 1000 more rows plus 99 per row to discard

		if (burnin == TRUE){
			n = n*100+1000
		}
		
		# Setup matrix
		
        matr <- matrix(ncol = 2, nrow = n)
        
        x <- 0
        y <- 0
        
        matr[1, ] <- c(x+xmean, y+ymean)
        
		# Main loop to get random numbers

        for (i in 2:n) {
                # Sampling from 0 mean distribution 
        
                x <- stdev*rnorm(1, r * y, sqrt(1 - r^2))
                y <- stdev*rnorm(1, r * x, sqrt(1 - r^2))
                
                # Shifting the mean base  
                matr[i, ] <- c(x+xmean, y+ymean)
        
        }
        
		# If burn in is on, dump first thousand rows and only select every 100th row

		if (burnin == TRUE){
			matr <- matr[1001:n,]
			n <- n-1000
			new <- n/100
			newmatr <- matrix(ncol = 2, nrow = new)
			for (i in 1:new){
				newmatr[i, ] <- matr[i*100, ]
			}
			matr = newmatr
		}

        matr
}


writeLines ("No Burn In\n")
gs<-GibbsSamplerFromMNormal(100,-.15,.5,-.5)
print(gs)

writeLines ("\n\nBurn In\n")
gs<-GibbsSamplerFromMNormal(100,-.15,.5,-.5,1,TRUE)
print(gs)
