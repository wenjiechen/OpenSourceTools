/.*Rank.*Rating.*Title.*/!d
s/<\/tr>/#/g
s/<\/\{0,1\}[[:alpha:]]\{1,\}[^>]*>/ /g
s/[[:space:]]\{2,\}/|/g
s/[^#]*\(#|.*|#\)[^#]*/\1/g
s/|\([0-9]\{1,\}\)\.|/|\1|/g
s/(\([0-9]\{4\}\)\/*[^)]*)/\1/g
s/\([0-9]\{1,3\}\),/\1/g
s/|#|/\n/g
s/#|//
s/|#//
s/&#x27;/'/g
s/&#x[0-9ABCEDF]\{2\};/*/g