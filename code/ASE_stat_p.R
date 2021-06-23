library(data.table)
library(ggplot2)
setwd("E:/OneDrive/DataAnalysis/Cattle_RNASeq/ASE")
chisq_fun <- function(x){
  out <- chisq.test(x, p = c(0.5, 0.5))
  return(c(as.numeric(out$statistic), out$p.value))
}
## chisq test, FDR adjust and output p values
dir_out <- "chisq_p_value"
# dir_out <- "strict.chisq_p_value"
dir.create(dir_out)
for(i in list.files(pattern = "ASE.table.filter.txt")){
# for(i in list.files(pattern = "ASE.table.filter.strict.txt")){
  print(i)
  ase <- fread(i)
  test <- t(apply(ase[, c(6,7)], 1, chisq_fun))
  colnames(test) <- c("chisq", "p")
  p_adjust <- p.adjust(test[,2], method = "fdr")
  test <- cbind(test, p_adjust)
  out <- cbind(ase, test)
  fwrite(out, paste(dir_out, "/", sub(".txt", "", i, fixed = TRUE), ".p.value.txt", sep = ""), sep = "\t")
}
