let multiple_upto n r =
  let rec aux idx =
    if idx > r
    then
      false
    else
    if n mod idx = 0 then
      true
    else
      aux (idx + 1)
  in aux 2
;;

