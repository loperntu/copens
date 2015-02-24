#!/usr/bin/env Rscript
args=commandArgs(trailingOnly=T)

df1=read.table(args[1])
df2=read.table(args[2])
df=merge(df1,df2)
for(row in df[,1]){
    cat(row)
    cat('\n')
}
