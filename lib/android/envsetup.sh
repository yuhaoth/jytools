function myhelp() # Local help function , to list my local function usage
{
	hmm;
	cat $HOME/lib/android/envsetup.sh | sed -n "/^function /s/function \([a-z_]*\).*\#\(.*\)/\- \1: \t\2/p" | sort
}
function gen_androd_signed_user_key() 	#generate the user signed keys 
{
	echo "Not Implement "
}
#export PS1='[android]${debian_chroot:+($debian_chroot)}\u@\h:\w\$'
#export OUT_DIR=$TARGET_PRODUCT
_mp_complete_update()
{
    export complete_mp_file=$OUT/.mp_complete
    mkdir -p $OUT
    make -qp  2>/dev/null | awk -F':' '/^[a-zA-Z0-9][^$#\/\t=]*:([^=]|$)/ \
          {split($1,A,/ /);for(i in A)print A[i]}' >$complete_mp_file
}
_mp()
{
    local  cur

    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}
    mkdir -p $OUT
    
    export complete_mp_file=$OUT/.mp_complete
    if [ -f $complete_mp_file ] 
    then
	complete_words=$( cat $complete_mp_file )
    else
	complete_words=$(make -qp  2>/dev/null | awk -F':' '/^[a-zA-Z0-9][^$#\/\t=]*:([^=]|$)/ \
          {split($1,A,/ /);for(i in A)print A[i]}' |  tee $complete_mp_file)
	
    fi
    

    COMPREPLY=( $( compgen -W "$complete_words" \
        -- "$cur" ) )

} &&
complete -F _mp m mp
. $HOME/lib/android/repo.bash_completion
. $HOME/lib/android/sign

jy_all_format-patches()
{
    outpatches_dir=/tmp/patches/
    output_pakage=$PWD/$2.tgz
    rm -rf $outpatches_dir
    pushd $PWD
    for i in $(cat $TOP/.repo/project.list)
    do
        output_dir=$outpatches_dir/$i
        croot && cd $i && mkdir -p $output_dir  && git format-patch -o $output_dir $1 
    done
    
    cd $outpatches_dir
    find . -name *.patch | xargs -l  dirname | sort -u >$outpatches_dir/project.list
    tar cvfz $output_pakage project.list $(find . -name *.patch)

    popd
}
