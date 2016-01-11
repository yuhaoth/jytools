Using built-in specs.
Usage: arm-none-eabi-gcc [options] file...
Options:
  -pass-exit-codes         Exit with highest error code from a phase
  --help                   Display this information
  --target-help            Display target specific command line options
  --help={target|optimizers|warnings|params|[^]{joined|separate|undocumented}}[,...]
                           Display specific types of command line options
  --version                Display compiler version information
  -dumpspecs               Display all of the built in spec strings
  -dumpversion             Display the version of the compiler
  -dumpmachine             Display the compiler's target processor
  -print-search-dirs       Display the directories in the compiler's search path
  -print-libgcc-file-name  Display the name of the compiler's companion library
  -print-file-name=<lib>   Display the full path to library <lib>
  -print-prog-name=<prog>  Display the full path to compiler component <prog>
  -print-multi-directory   Display the root directory for versions of libgcc
  -print-multi-lib         Display the mapping between command line options and
                           multiple library search directories
  -print-multi-os-directory Display the relative path to OS libraries
  -print-sysroot           Display the target libraries directory
  -print-sysroot-headers-suffix Display the sysroot suffix used to find headers
  -Wa,<options>            Pass comma-separated <options> on to the assembler
  -Wp,<options>            Pass comma-separated <options> on to the preprocessor
  -Wl,<options>            Pass comma-separated <options> on to the linker
  -Xassembler <arg>        Pass <arg> on to the assembler
  -Xpreprocessor <arg>     Pass <arg> on to the preprocessor
  -Xlinker <arg>           Pass <arg> on to the linker
  -combine                 Pass multiple source files to compiler at once
  -save-temps              Do not delete intermediate files
  -pipe                    Use pipes rather than intermediate files
  -time                    Time the execution of each subprocess
  -specs=<file>            Override built-in specs with the contents of <file>
  -std=<standard>          Assume that the input sources are for <standard>
  --sysroot=<directory>    Use <directory> as the root directory for headers
                           and libraries
  -B <directory>           Add <directory> to the compiler's search paths
  -b <machine>             Run gcc for target <machine>, if installed
  -V <version>             Run gcc version number <version>, if installed
  -v                       Display the programs invoked by the compiler
  -###                     Like -v but options quoted and commands not executed
  -E                       Preprocess only; do not compile, assemble or link
  -S                       Compile only; do not assemble or link
  -c                       Compile and assemble, but do not link
  -o <file>                Place the output into <file>
  -x <language>            Specify the language of the following input files
                           Permissible languages include: c c++ assembler none
                           'none' means revert to the default behavior of
                           guessing the language based on the file's extension

Options starting with -g, -f, -m, -O, -W, or --param are automatically
 passed on to the various sub-processes invoked by arm-none-eabi-gcc.  In order to pass
 other options on to these processes the -W<letter> options must be used.

Target: arm-none-eabi
Configured with: /scratch/julian/2010q1-release-eabi-lite/src/gcc-4.4-2010q1/configure --build=i686-pc-linux-gnu --host=i686-pc-linux-gnu --target=arm-none-eabi --enable-threads --disable-libmudflap --disable-libssp --disable-libstdcxx-pch --enable-extra-sgxxlite-multilibs --with-gnu-as --with-gnu-ld --with-specs='%{O2:%{!fno-remove-local-statics: -fremove-local-statics}} %{O*:%{O|O0|O1|O2|Os:;:%{!fno-remove-local-statics: -fremove-local-statics}}}' --enable-languages=c,c++ --disable-shared --disable-lto --with-newlib --with-pkgversion='Sourcery G++ Lite 2010q1-188' --with-bugurl=https://support.codesourcery.com/GNUToolchain/ --disable-nls --prefix=/opt/codesourcery --with-headers=yes --with-sysroot=/opt/codesourcery/arm-none-eabi --with-build-sysroot=/scratch/julian/2010q1-release-eabi-lite/install/arm-none-eabi --with-gmp=/scratch/julian/2010q1-release-eabi-lite/obj/host-libs-2010q1-188-arm-none-eabi-i686-pc-linux-gnu/usr --with-mpfr=/scratch/julian/2010q1-release-eabi-lite/obj/host-libs-2010q1-188-arm-none-eabi-i686-pc-linux-gnu/usr --with-ppl=/scratch/julian/2010q1-release-eabi-lite/obj/host-libs-2010q1-188-arm-none-eabi-i686-pc-linux-gnu/usr --with-host-libstdcxx='-static-libgcc -Wl,-Bstatic,-lstdc++,-Bdynamic -lm' --with-cloog=/scratch/julian/2010q1-release-eabi-lite/obj/host-libs-2010q1-188-arm-none-eabi-i686-pc-linux-gnu/usr --disable-libgomp --enable-poison-system-directories --with-build-time-tools=/scratch/julian/2010q1-release-eabi-lite/install/arm-none-eabi/bin --with-build-time-tools=/scratch/julian/2010q1-release-eabi-lite/install/arm-none-eabi/bin
Thread model: single
gcc version 4.4.1 (Sourcery G++ Lite 2010q1-188) 
COLLECT_GCC_OPTIONS='-v' '-fhelp'

 /opt/CodeSourcery/Sourcery_G++_Lite/bin/../libexec/gcc/arm-none-eabi/4.4.1/cc1 -quiet -v -iprefix /opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/ -isysroot /opt/CodeSourcery/Sourcery_G++_Lite/bin/../arm-none-eabi -D__USES_INITFINI__ help-dummy -quiet -dumpbase help-dummy -auxbase help-dummy -version -fhelp -o /tmp/cccb7VSf.s
The following options are specific to just the language Ada:
  -fRTS=                      
  -feliminate-unused-debug-types Perform unused type elimination in debug info
  -gant                       
  -gdwarf+                    
  -gnat<options>              Specify options to GNAT
  -gnatO                      
  -nostdlib                   

The following options are specific to just the language C:
  -lang-asm                   

The following options are specific to just the language C++:
 None found.  Use --help=C++ to show *all* the options supported by the C++ front-end

The following options are specific to just the language Fortran:
  -J<directory>               Put MODULE files in 'directory'
  -Waliasing                  Warn about possible aliasing of dummy arguments
  -Walign-commons             Warn about alignment of COMMON blocks
  -Wampersand                 Warn about missing ampersand in continued
                              character constants
  -Warray-temporaries         Warn about creation of array temporaries
  -Wcharacter-truncation      Warn about truncated character expressions
  -Wimplicit-interface        Warn about calls with implicit interface
  -Wintrinsic-shadow          Warn if a user-procedure has the same name as an
                              intrinsic
  -Wintrinsics-std            Warn on intrinsics not part of the selected
                              standard
  -Wline-truncation           Warn about truncated source lines
  -Wsurprising                Warn about "suspicious" constructs
  -Wtabs                      Permit nonconforming uses of the tab character
  -Wunderflow                 Warn about underflow of numerical constant
                              expressions
  -cpp                        Enable preprocessing
  -falign-commons             Enable alignment of COMMON blocks
  -fall-intrinsics            All intrinsics procedures are available
                              regardless of selected standard
  -fallow-leading-underscore  
  -fautomatic                 Do not treat local variables and COMMON blocks as
                              if they were named in SAVE statements
  -fbackslash                 Specify that backslash in string introduces an
                              escape character
  -fbacktrace                 Produce a backtrace when a runtime error is
                              encountered
  -fblas-matmul-limit=        -fblas-matmul-limit=<n>        Size of the
                              smallest matrix for which matmul will use BLAS
  -fcheck-array-temporaries   Produce a warning at runtime if a array temporary
                              has been created for a procedure argument
  -fconvert=big-endian        Use big-endian format for unformatted files
  -fconvert=little-endian     Use little-endian format for unformatted files
  -fconvert=native            Use native format for unformatted files
  -fconvert=swap              Swap endianness for unformatted files
  -fcray-pointer              Use the Cray Pointer extension
  -fd-lines-as-code           Ignore 'D' in column one in fixed form
  -fd-lines-as-comments       Treat lines with 'D' in column one as comments
  -fdefault-double-8          Set the default double precision kind to an 8
                              byte wide type
  -fdefault-integer-8         Set the default integer kind to an 8 byte wide
                              type
  -fdefault-real-8            Set the default real kind to an 8 byte wide type
  -fdollar-ok                 Allow dollar signs in entity names
  -fdump-core                 Dump a core file when a runtime error occurs
  -fdump-parse-tree           Display the code tree after parsing
  -fexternal-blas             Specify that an external BLAS library should be
                              used for matmul calls on large-size arrays
  -ff2c                       Use f2c calling convention
  -ffixed-form                Assume that the source file is fixed form
  -ffixed-line-length-<n>     	Use n as character line width in fixed mode
  -ffixed-line-length-none    Allow arbitrary character line width in fixed mode
  -ffpe-trap=[..]             Stop on following floating point exceptions
  -ffree-form                 Assume that the source file is free form
  -ffree-line-length-<n>      	Use n as character line width in free mode
  -ffree-line-length-none     Allow arbitrary character line width in free mode
  -fimplicit-none             Specify that no implicit typing is allowed,
                              unless overridden by explicit IMPLICIT statements
  -finit-character=           -finit-character=<n> Initialize local character
                              variables to ASCII value n
  -finit-integer=             -finit-integer=<n> Initialize local integer
                              variables to n
  -finit-local-zero           Initialize local variables to zero (from g77)
  -finit-logical=             -finit-logical=<true|false> Initialize local
                              logical variables
  -finit-real=                -finit-real=<zero|nan|inf|-inf> Initialize local
                              real variables
  -fintrinsic-modules-path    Specify where to find the compiled intrinsic
                              modules
  -fmax-array-constructor=    -fmax-array-constructor=<n>        Maximum number
                              of objects in an array constructor
  -fmax-errors=<n>            Maximum number of errors to report
  -fmax-identifier-length=<n> Maximum identifier length
  -fmax-stack-var-size=<n>    Size in bytes of the largest array that will be
                              put on the stack
  -fmax-subrecord-length=<n>  Maximum length for subrecords
  -fmodule-private            Set default accessibility of module entities to
                              PRIVATE.
  -fpack-derived              Try to lay out derived types as compactly as
                              possible
  -frange-check               Enable range checking during compilation
  -frecord-marker=4           Use a 4-byte record marker for unformatted files
  -frecord-marker=8           Use an 8-byte record marker for unformatted files
  -frecursive                 Allocate local variables on the stack to allow
                              indirect recursion
  -frepack-arrays             Copy array sections into a contiguous block on
                              procedure entry
  -fsecond-underscore         Append a second underscore if the name already
                              contains an underscore
  -fsign-zero                 Apply negative sign to zero values
  -funderscoring              Append underscores to externally visible names
  -nocpp                      Disable preprocessing
  -static-libgfortran         Statically link the GNU Fortran helper library
                              (libgfortran)
  -std=f2003                  Conform to the ISO Fortran 2003 standard
  -std=f2008                  Conform to the ISO Fortran 2008 standard
  -std=f95                    Conform to the ISO Fortran 95 standard
  -std=gnu                    Conform to nothing in particular
  -std=legacy                 Accept extensions to support legacy code

The following options are specific to just the language Java:
  -MD_                        
  -MMD_                       
  -Wall-deprecation           
  -Wall-javadoc               
  -Wassert-identifier         
  -Wboxing                    
  -Wchar-concat               
  -Wcondition-assign          
  -Wconstructor-name          
  -Wdep-ann                   
  -Wdiscouraged               
  -Wempty-block               
  -Wenum-identifier           
  -Wenum-switch               
  -Wextraneous-semicolon      Warn if deprecated empty statements are found
  -Wfallthrough               
  -Wfield-hiding              
  -Wfinal-bound               
  -Wfinally                   
  -Wforbidden                 
  -Whiding                    
  -Windirect-static           
  -Wintf-annotation           
  -Wintf-non-inherited        
  -Wjavadoc                   
  -Wlocal-hiding              
  -Wmasked-catch-block        
  -Wnls                       
  -Wno-effect-assign          
  -Wnull                      
  -Wout-of-date               Warn if .class files are out of date
  -Wover-ann                  
  -Wparam-assign              
  -Wpkg-default-method        
  -Wraw                       
  -Wredundant-modifiers       Warn if modifiers are specified when not necessary
  -Wserial                    
  -Wspecial-param-hiding      
  -Wstatic-access             
  -Wstatic-receiver           
  -Wsuppress                  
  -Wsynthetic-access          
  -Wtasks                     
  -Wtype-hiding               
  -Wuncheck                   
  -Wunnecessary-else          
  -Wunqualified-field         
  -Wunused                    Enable all -Wunused- warnings
  -Wunused-argument           
  -Wunused-import             
  -Wunused-label              Warn when a label is unused
  -Wunused-local              
  -Wunused-private            
  -Wunused-thrown             
  -Wuseless-type-check        
  -Wvarargs-cast              
  -Wwarning-token             
  --CLASSPATH                 Deprecated; use --classpath instead
  -fassert                    Permit the use of the assert keyword
  -fassume-compiled           
  -fassume-compiled=          
  -faux-classpath             
  --bootclasspath=<path>      Replace system path
  -fbootstrap-classes         Generated should be loaded by bootstrap loader
  -fcheck-references          Generate checks for references to NULL
  --classpath=<path>          Set class path
  -fcompile-resource=         
  -fdisable-assertions        
  -fdisable-assertions=       
  -femit-class-file           Output a class file
  -femit-class-files          Alias for -femit-class-file
  -fenable-assertions         
  -fenable-assertions=        
  --encoding=<encoding>       Choose input encoding (defaults from your locale)
  --extdirs=<path>            Set the extension directory path
  -ffilelist-file             Input file is a file with a list of filenames to
                              compile
  -fforce-classes-archive-check Always check for non gcj generated classes
                              archives
  -fhash-synchronization      Assume the runtime uses a hash table to map an
                              object to its synchronization structure
  -findirect-classes          Generate instances of Class at runtime
  -findirect-dispatch         Use offset tables for virtual method calls
  -finline-functions          Integrate simple functions into their callers
  -fjni                       Assume native functions are implemented using JNI
  -foptimize-static-class-initialization Enable optimization of static class
                              initialization code
  -foutput-class-dir=         
  -freduced-reflection        Reduce the amount of reflection meta-data
                              generated
  -fsaw-java-file             
  -fsource-filename=          
  -fsource=                   Set the source language version
  -fstore-check               Enable assignability checks for stores into
                              object arrays
  -ftarget=                   Set the target VM version
  -fuse-boehm-gc              Generate code for the Boehm GC
  -fuse-divide-subroutine     Call a library routine to do integer divisions
  -version                    Display the compiler's version

The following options are specific to just the language ObjC:
 None found.  Use --help=ObjC to show *all* the options supported by the ObjC front-end

The following options are specific to just the language ObjC++:
  -fobjc-call-cxx-cdtors      Generate special Objective-C methods to
                              initialize/destroy non-POD C++ ivars, if needed

The following options are language-related:
  --output-pch=               
  -A<question>=<answer>       Assert the <answer> to <question>.  Putting '-'
                              before <question> disables the <answer> to
                              <question>
  -C                          Do not discard comments
  -CC                         Do not discard comments in macro expansions
  -D<macro>[=<val>]           Define a <macro> with <val> as its value.  If
                              just <macro> is given, <val> is taken to be 1
  -E                          
  -F <dir>                    Add <dir> to the end of the main framework
                              include path
  -H                          Print the name of header files as they are used
  -I <dir>                    Add <dir> to the end of the main include path
  -M                          Generate make dependencies
  -MD                         Generate make dependencies and compile
  -MF <file>                  Write dependency output to the given file
  -MG                         Treat missing header files as generated files
  -MM                         Like -M but ignore system header files
  -MMD                        Like -MD but ignore system header files
  -MP                         Generate phony targets for all headers
  -MQ <target>                Add a MAKE-quoted target
  -MT <target>                Add an unquoted target
  -P                          Do not generate #line directives
  -U<macro>                   Undefine <macro>
  -Wabi                       Warn about things that will change when compiling
                              with an ABI-compliant compiler
  -Waddress                   Warn about suspicious uses of memory addresses
  -Wall                       Enable most warning messages
  -Wassign-intercept          Warn whenever an Objective-C assignment is being
                              intercepted by the garbage collector
  -Wbad-function-cast         Warn about casting functions to incompatible types
  -Wbuiltin-macro-redefined   Warn when a built-in preprocessor macro is
                              undefined or redefined
  -Wc++-compat                Warn about C constructs that are not in the
                              common subset of C and C++
  -Wc++0x-compat              Warn about C++ constructs whose meaning differs
                              between ISO C++ 1998 and ISO C++ 200x
  -Wcast-qual                 Warn about casts which discard qualifiers
  -Wchar-subscripts           Warn about subscripts whose type is "char"
  -Wclobbered                 Warn about variables that might be changed by
                              "longjmp" or "vfork"
  -Wcomment                   Warn about possibly nested block comments, and
                              C++ comments spanning more than one physical line
  -Wcomments                  Synonym for -Wcomment
  -Wconversion                Warn for implicit type conversions that may
                              change a value
  -Wctor-dtor-privacy         Warn when all constructors and destructors are
                              private
  -Wdeclaration-after-statement Warn when a declaration is found after a
                              statement
  -Wdeprecated                Warn if a deprecated compiler feature, class,
                              method, or field is used
  -Wdiv-by-zero               Warn about compile-time integer division by zero
  -Weffc++                    Warn about violations of Effective C++ style rules
  -Wempty-body                Warn about an empty body in an if or else
                              statement
  -Wendif-labels              Warn about stray tokens after #elif and #endif
  -Wenum-compare              Warn about comparison of different enum types
  -Werror                     Treat all warnings as errors
  -Werror-implicit-function-declaration This switch is deprecated; use
                              -Werror=implicit-function-declaration instead
  -Wfloat-equal               Warn if testing floating point numbers for
                              equality
  -Wformat                    Warn about printf/scanf/strftime/strfmon format
                              string anomalies
  -Wformat-contains-nul       Warn about format strings that contain NUL bytes
  -Wformat-extra-args         Warn if passing too many arguments to a function
                              for its format string
  -Wformat-nonliteral         Warn about format strings that are not literals
  -Wformat-security           Warn about possible security problems with format
                              functions
  -Wformat-y2k                Warn about strftime formats yielding 2-digit years
  -Wformat-zero-length        Warn about zero-length formats
  -Wformat=                   
  -Wignored-qualifiers        Warn whenever type qualifiers are ignored.
  -Wimplicit                  
  -Wimplicit-function-declaration Warn about implicit function declarations
  -Wimplicit-int              Warn when a declaration does not specify a type
  -Wimport                    
  -Winit-self                 Warn about variables which are initialized to
                              themselves
  -Wint-to-pointer-cast       Warn when there is a cast to a pointer from an
                              integer of a different size
  -Winvalid-offsetof          Warn about invalid uses of the "offsetof" macro
  -Winvalid-pch               Warn about PCH files that are found but not used
  -Wlong-long                 Do not warn about using "long long" when -pedantic
  -Wmain                      Warn about suspicious declarations of "main"
  -Wmissing-braces            Warn about possibly missing braces around
                              initializers
  -Wmissing-declarations      Warn about global functions without previous
                              declarations
  -Wmissing-field-initializers Warn about missing fields in struct initializers
  -Wmissing-format-attribute  Warn about functions which might be candidates
                              for format attributes
  -Wmissing-include-dirs      Warn about user-specified include directories
                              that do not exist
  -Wmissing-parameter-type    Warn about function parameters declared without a
                              type specifier in K&R-style functions
  -Wmissing-prototypes        Warn about global functions without prototypes
  -Wmultichar                 Warn about use of multi-character character
                              constants
  -Wnested-externs            Warn about "extern" declarations not at file scope
  -Wnon-template-friend       Warn when non-templatized friend functions are
                              declared within a template
  -Wnon-virtual-dtor          Warn about non-virtual destructors
  -Wnonnull                   Warn about NULL being passed to argument slots
                              marked as requiring non-NULL
  -Wnormalized=<id|nfc|nfkc>  Warn about non-normalised Unicode strings
  -Wold-style-cast            Warn if a C-style cast is used in a program
  -Wold-style-declaration     Warn for obsolescent usage in a declaration
  -Wold-style-definition      Warn if an old-style parameter definition is used
  -Woverlength-strings        Warn if a string is longer than the maximum
                              portable length specified by the standard
  -Woverloaded-virtual        Warn about overloaded virtual function names
  -Woverride-init             Warn about overriding initializers without side
                              effects
  -Wpacked-bitfield-compat    Warn about packed bit-fields whose offset changed
                              in GCC 4.4
  -Wparentheses               Warn about possibly missing parentheses
  -Wpmf-conversions           Warn when converting the type of pointers to
                              member functions
  -Wpointer-arith             Warn about function pointer arithmetic
  -Wpointer-sign              Warn when a pointer differs in signedness in an
                              assignment
  -Wpointer-to-int-cast       Warn when a pointer is cast to an integer of a
                              different size
  -Wpragmas                   Warn about misuses of pragmas
  -Wprotocol                  Warn if inherited methods are unimplemented
  -Wpsabi                     
  -Wredundant-decls           Warn about multiple declarations of the same
                              object
  -Wreorder                   Warn when the compiler reorders code
  -Wreturn-type               Warn whenever a function's return type defaults
                              to "int" (C), or about inconsistent return types
                              (C++)
  -Wselector                  Warn if a selector has multiple methods
  -Wsequence-point            Warn about possible violations of sequence point
                              rules
  -Wsign-compare              Warn about signed-unsigned comparisons
  -Wsign-conversion           Warn for implicit type conversions between signed
                              and unsigned integers
  -Wsign-promo                Warn when overload promotes from unsigned to
                              signed
  -Wstrict-null-sentinel      Warn about uncasted NULL used as sentinel
  -Wstrict-prototypes         Warn about unprototyped function declarations
  -Wstrict-selector-match     Warn if type signatures of candidate methods do
                              not match exactly
  -Wsync-nand                 Warn when __sync_fetch_and_nand and
                              __sync_nand_and_fetch built-in functions are used
  -Wsynth                     Deprecated.  This switch has no effect
  -Wsystem-headers            Do not suppress warnings from system headers
  -Wtraditional               Warn about features not present in traditional C
  -Wtraditional-conversion    Warn of prototypes causing type conversions
                              different from what would happen in the absence
                              of prototype
  -Wtrigraphs                 Warn if trigraphs are encountered that might
                              affect the meaning of the program
  -Wundeclared-selector       Warn about @selector()s without previously
                              declared methods
  -Wundef                     Warn if an undefined macro is used in an #if
                              directive
  -Wunknown-pragmas           Warn about unrecognized pragmas
  -Wunused-macros             Warn about macros defined in the main file that
                              are not used
  -Wvariadic-macros           Do not warn about using variadic macros when
                              -pedantic
  -Wvla                       Warn if a variable length array is used
  -Wvolatile-register-var     Warn when a register variable is declared volatile
  -Wwrite-strings             In C++, nonzero means warn about deprecated
                              conversion from string literals to `char *'.  In
                              C, similar warning, except that the conversion is
                              of course not deprecated by the ISO C standard.
  -ansi                       A synonym for -std=c89 (for C) or -std=c++98 (for
                              C++)
  -d<letters>                 Enable dumps from specific passes of the compiler
  -faccess-control            Enforce class member access control semantics
  -fall-virtual               
  -falt-external-templates    Change when template instances are emitted
  -fasm                       Recognize the "asm" keyword
  -fbuiltin                   Recognize built-in functions
  -fbuiltin-                  
  -fcheck-new                 Check the return value of new
  -fcond-mismatch             Allow the arguments of the '?' operator to have
                              different types
  -fconserve-space            Reduce the size of object files
  -fconst-string-class=<name> Use class <name> for constant strings
  -fdefault-inline            Inline member functions by default
  -fdirectives-only           Preprocess directives only.
  -fdollars-in-identifiers    Permit '$' as an identifier character
  -felide-constructors        
  -femit-struct-debug-baseonly Aggressive reduced debug info for structs
  -femit-struct-debug-detailed=<spec-list> Detailed reduced debug info for
                              structs
  -femit-struct-debug-reduced Conservative reduced debug info for structs
  -fenforce-eh-specs          Generate code to check exception specifications
  -fenum-int-equiv            
  -fexec-charset=<cset>       Convert all strings and character constants to
                              character set <cset>
  -fextended-identifiers      Permit universal character names (\u and \U) in
                              identifiers
  -fexternal-templates        
  -ffor-scope                 Scope of for-init-statement variables is local to
                              the loop
  -ffreestanding              Do not assume that standard C libraries and
                              "main" exist
  -ffriend-injection          Inject friend functions into enclosing namespace
  -fgnu-keywords              Recognize GNU-defined keywords
  -fgnu-runtime               Generate code for GNU runtime environment
  -fgnu89-inline              Use traditional GNU semantics for inline functions
  -fguiding-decls             
  -fhandle-exceptions         
  -fhonor-std                 
  -fhosted                    Assume normal C execution environment
  -fhuge-objects              Enable support for huge objects
  -fimplement-inlines         Export functions even if they can be inlined
  -fimplicit-inline-templates Emit implicit instantiations of inline templates
  -fimplicit-templates        Emit implicit instantiations of templates
  -finput-charset=<cset>      Specify the default character set for source files
  -flabels-ok                 
  -flax-vector-conversions    Allow implicit conversions between vectors with
                              differing numbers of subparts and/or differing
                              element types.
  -fms-extensions             Don't warn about uses of Microsoft extensions
  -fname-mangling-version-    
  -fnew-abi                   
  -fnext-runtime              Generate code for NeXT (Apple Mac OS X) runtime
                              environment
  -fnil-receivers             Assume that receivers of Objective-C messages may
                              be nil
  -fnonansi-builtins          
  -fnonnull-objects           
  -fobjc-direct-dispatch      Allow fast jumps to the message dispatcher
  -fobjc-exceptions           Enable Objective-C exception and synchronization
                              syntax
  -fobjc-gc                   Enable garbage collection (GC) in Objective-C/
                              Objective-C++ programs
  -fobjc-sjlj-exceptions      Enable Objective-C setjmp exception handling
                              runtime
  -fopenmp                    Enable OpenMP (implies -frecursive in Fortran)
  -foperator-names            Recognize C++ keywords like "compl" and "xor"
  -foptional-diags            Enable optional diagnostics
  -fpch-deps                  
  -fpch-preprocess            Look for and use PCH files even when preprocessing
  -fpermissive                Downgrade conformance errors to warnings
  -fpreprocessed              Treat the input file as already preprocessed
  -fremove-local-statics      Convert function-local static variables to
                              automatic variables when it is safe to do so
  -freplace-objc-classes      Used in Fix-and-Continue mode to indicate that
                              object files may be swapped in at runtime
  -frepo                      Enable automatic template instantiation
  -frtti                      Generate run time type descriptor information
  -fshort-double              Use the same size for double as for float
  -fshort-enums               Use the narrowest integer type possible for
                              enumeration types
  -fshort-wchar               Force the underlying type for "wchar_t" to be
                              "unsigned short"
  -fshow-column               Show column numbers in diagnostics, when
                              available.  Default off
  -fsigned-bitfields          When "signed" or "unsigned" is not given make the
                              bitfield signed
  -fsigned-char               Make "char" signed by default
  -fsquangle                  
  -fstats                     Display statistics accumulated during compilation
  -fstrict-prototype          
  -ftabstop=<number>          Distance between tab stops for column reporting
  -ftemplate-depth-<number>   Specify maximum template instantiation depth
  -fthis-is-variable          
  -fno-threadsafe-statics     Do not generate thread-safe code for initializing
                              local statics
  -funsigned-bitfields        When "signed" or "unsigned" is not given make the
                              bitfield unsigned
  -funsigned-char             Make "char" unsigned by default
  -fuse-cxa-atexit            Use __cxa_atexit to register destructors
  -fuse-cxa-get-exception-ptr Use __cxa_get_exception_ptr in exception handling
  -fvisibility-inlines-hidden Marks all inlined methods as having hidden
                              visibility
  -fvisibility-ms-compat      Changes visibility to match Microsoft Visual
                              Studio by default
  -fvtable-gc                 Discard unused virtual functions
  -fvtable-thunks             Implement vtables using thunks
  -fweak                      Emit common-like symbols as weak symbols
  -fwide-exec-charset=<cset>  Convert all wide strings and character constants
                              to character set <cset>
  -fworking-directory         Generate a #line directive pointing at the
                              current working directory
  -fxref                      Emit cross referencing information
  -fzero-link                 Generate lazy class lookup (via objc_getClass())
                              for use in Zero-Link mode
  -gen-decls                  Dump declarations to a .decl file
  -idirafter <dir>            Add <dir> to the end of the system include path
  -imacros <file>             Accept definition of macros in <file>
  -imultilib                  -imultilib <dir> Set <dir> to be the multilib
                              include subdirectory
  -include <file>             Include the contents of <file> before other files
  -iprefix <path>             Specify <path> as a prefix for next two options
  -iquote <dir>               Add <dir> to the end of the quote include path
  -isysroot <dir>             Set <dir> to be the system root directory
  -isystem <dir>              Add <dir> to the start of the system include path
  -iwithprefix <dir>          Add <dir> to the end of the system include path
  -iwithprefixbefore <dir>    Add <dir> to the end of the main include path
  -lang-objc                  
  -nostdinc                   Do not search standard system include directories
                              (those specified with -isystem will still be used)
  -nostdinc++                 Do not search standard system include directories
                              for C++
  -o <file>                   Place output into <file>
  -pedantic                   Issue warnings needed for strict compliance to
                              the standard
  -pedantic-errors            Like -pedantic but issue them as errors
  -print-objc-runtime-info    Generate C header of platform-specific features
  -print-pch-checksum         Print a checksum of the executable for PCH
                              validity checking, and stop
  -remap                      Remap file names when including files
  -std=c++0x                  Conform to the ISO 1998 C++ standard, with
                              extensions that are likely to become a part of
                              the upcoming ISO C++ standard, dubbed C++0x. Note
                              that the extensions enabled by this mode are
                              experimental and may be removed in future
                              releases of GCC.
  -std=c++98                  Conform to the ISO 1998 C++ standard
  -std=c89                    Conform to the ISO 1990 C standard
  -std=c99                    Conform to the ISO 1999 C standard
  -std=c9x                    Deprecated in favor of -std=c99
  -std=gnu++0x                Conform to the ISO 1998 C++ standard, with GNU
                              extensions and extensions that are likely to
                              become a part of the upcoming ISO C++ standard,
                              dubbed C++0x. Note that the extensions enabled by
                              this mode are experimental and may be removed in
                              future releases of GCC.
  -std=gnu++98                Conform to the ISO 1998 C++ standard with GNU
                              extensions
  -std=gnu89                  Conform to the ISO 1990 C standard with GNU
                              extensions
  -std=gnu99                  Conform to the ISO 1999 C standard with GNU
                              extensions
  -std=gnu9x                  Deprecated in favor of -std=gnu99
  -std=iso9899:1990           Conform to the ISO 1990 C standard
  -std=iso9899:199409         Conform to the ISO 1990 C standard as amended in
                              1994
  -std=iso9899:1999           Conform to the ISO 1999 C standard
  -std=iso9899:199x           Deprecated in favor of -std=iso9899:1999
  -traditional-cpp            Enable traditional preprocessing
  -trigraphs                  Support ISO C trigraphs
  -undef                      Do not predefine system-specific and GCC-specific
                              macros
  -v                          Enable verbose output
  -w                          Suppress warnings

The --param option recognizes the following as parameters:
  sra-max-structure-size      The maximum structure size (in bytes) for which
                              GCC will use by-element copies
  sra-max-structure-count     The maximum number of structure fields for which
                              GCC will use by-element copies
  sra-field-structure-ratio   The threshold ratio between instantiated fields
                              and the total structure size
  struct-reorg-cold-struct-ratio The threshold ratio between current and
                              hottest structure counts
  predictable-branch-outcome  Maximal esitmated outcome of branch considered
                              predictable
  max-inline-insns-single     The maximum number of instructions in a single
                              function eligible for inlining
  max-inline-insns-auto       The maximum number of instructions when
                              automatically inlining
  max-inline-insns-recursive  The maximum number of instructions inline
                              function can grow to via recursive inlining
  max-inline-insns-recursive-auto The maximum number of instructions non-inline
                              function can grow to via recursive inlining
  max-inline-recursive-depth  The maximum depth of recursive inlining for
                              inline functions
  max-inline-recursive-depth-auto The maximum depth of recursive inlining for
                              non-inline functions
  min-inline-recursive-probability Inline recursively only when the probability
                              of call being executed exceeds the parameter
  max-variable-expansions-in-unroller If -fvariable-expansion-in-unroller is
                              used, the maximum number of times that an
                              individual variable will be expanded during loop
                              unrolling
  min-vect-loop-bound         If -ftree-vectorize is used, the minimal loop
                              bound of a loop to be considered for vectorization
  max-delay-slot-insn-search  The maximum number of instructions to consider to
                              fill a delay slot
  max-delay-slot-live-search  The maximum number of instructions to consider to
                              find accurate live register information
  max-pending-list-length     The maximum length of scheduling's pending
                              operations list
  large-function-insns        The size of function body to be considered large
  large-function-growth       Maximal growth due to inlining of large function
                              (in percent)
  large-unit-insns            The size of translation unit to be considered
                              large
  inline-unit-growth          how much can given compilation unit grow because
                              of the inlining (in percent)
  ipcp-unit-growth            how much can given compilation unit grow because
                              of the interprocedural constant propagation (in
                              percent)
  inline-call-cost            expense of call operation relative to ordinary
                              arithmetic operations
  large-stack-frame           The size of stack frame to be considered large
  large-stack-frame-growth    Maximal stack frame growth due to inlining (in
                              percent)
  max-gcse-memory             The maximum amount of memory to be allocated by
                              GCSE
  max-gcse-passes             The maximum number of passes to make when doing
                              GCSE
  gcse-after-reload-partial-fraction The threshold ratio for performing partial
                              redundancy elimination after reload
  gcse-after-reload-critical-fraction The threshold ratio of critical edges
                              execution count that permit performing redundancy
                              elimination after reload
  max-unrolled-insns          The maximum number of instructions to consider to
                              unroll in a loop
  max-average-unrolled-insns  The maximum number of instructions to consider to
                              unroll in a loop on average
  max-unroll-times            The maximum number of unrollings of a single loop
  max-peeled-insns            The maximum number of insns of a peeled loop
  max-peel-times              The maximum number of peelings of a single loop
  max-completely-peeled-insns The maximum number of insns of a completely
                              peeled loop
  max-completely-peel-times   The maximum number of peelings of a single loop
                              that is peeled completely
  max-once-peeled-insns       The maximum number of insns of a peeled loop that
                              rolls only once
  max-unswitch-insns          The maximum number of insns of an unswitched loop
  max-unswitch-level          The maximum number of unswitchings in a single
                              loop
  max-iterations-to-track     Bound on the number of iterations the brute force
                              # of iterations analysis algorithm evaluates
  max-iterations-computation-cost Bound on the cost of an expression to compute
                              the number of iterations
  sms-max-ii-factor           A factor for tuning the upper bound that swing
                              modulo scheduler uses for scheduling a loop
  sms-dfa-history             The number of cycles the swing modulo scheduler
                              considers when checking conflicts using DFA
  sms-loop-average-count-threshold A threshold on the average loop count
                              considered by the swing modulo scheduler
  hot-bb-count-fraction       Select fraction of the maximal count of
                              repetitions of basic block in program given basic
                              block needs to have to be considered hot
  hot-bb-frequency-fraction   Select fraction of the maximal frequency of
                              executions of basic block in function given basic
                              block needs to have to be considered hot
  align-threshold             Select fraction of the maximal frequency of
                              executions of basic block in function given basic
                              block get alignment
  align-loop-iterations       Loops iterating at least selected number of
                              iterations will get loop alignement.
  max-predicted-iterations    The maximum number of loop iterations we predict
                              statically
  tracer-dynamic-coverage-feedback The percentage of function, weighted by
                              execution frequency, that must be covered by
                              trace formation. Used when profile feedback is
                              available
  tracer-dynamic-coverage     The percentage of function, weighted by execution
                              frequency, that must be covered by trace
                              formation. Used when profile feedback is not
                              available
  tracer-max-code-growth      Maximal code growth caused by tail duplication
                              (in percent)
  tracer-min-branch-ratio     Stop reverse growth if the reverse probability of
                              best edge is less than this threshold (in percent)
  tracer-min-branch-probability-feedback Stop forward growth if the probability
                              of best edge is less than this threshold (in
                              percent). Used when profile feedback is available
  tracer-min-branch-probability Stop forward growth if the probability of best
                              edge is less than this threshold (in percent).
                              Used when profile feedback is not available
  max-crossjump-edges         The maximum number of incoming edges to consider
                              for crossjumping
  min-crossjump-insns         The minimum number of matching instructions to
                              consider for crossjumping
  max-grow-copy-bb-insns      The maximum expansion factor when copying basic
                              blocks
  max-goto-duplication-insns  The maximum number of insns to duplicate when
                              unfactoring computed gotos
  max-cse-path-length         The maximum length of path considered in cse
  max-cse-insns               The maximum instructions CSE process before
                              flushing
  lim-expensive               The minimum cost of an expensive expression in
                              the loop invariant motion
  iv-consider-all-candidates-bound Bound on number of candidates below that all
                              candidates are considered in iv optimizations
  iv-max-considered-uses      Bound on number of iv uses in loop optimized in
                              iv optimizations
  iv-always-prune-cand-set-bound If number of candidates in the set is smaller,
                              we always try to remove unused ivs during its
                              optimization
  scev-max-expr-size          Bound on size of expressions used in the scalar
                              evolutions analyzer
  omega-max-vars              Bound on the number of variables in Omega
                              constraint systems
  omega-max-geqs              Bound on the number of inequalities in Omega
                              constraint systems
  omega-max-eqs               Bound on the number of equalities in Omega
                              constraint systems
  omega-max-wild-cards        Bound on the number of wild cards in Omega
                              constraint systems
  omega-hash-table-size       Bound on the size of the hash table in Omega
                              constraint systems
  omega-max-keys              Bound on the number of keys in Omega constraint
                              systems
  omega-eliminate-redundant-constraints When set to 1, use expensive methods to
                              eliminate all redundant constraints
  vect-max-version-for-alignment-checks Bound on number of runtime checks
                              inserted by the vectorizer's loop versioning for
                              alignment check
  vect-max-version-for-alias-checks Bound on number of runtime checks inserted
                              by the vectorizer's loop versioning for alias
                              check
  max-cselib-memory-locations The maximum memory locations recorded by cselib
  ggc-min-expand              Minimum heap expansion to trigger garbage
                              collection, as a percentage of the total size of
                              the heap
  ggc-min-heapsize            Minimum heap size before we start collecting
                              garbage, in kilobytes
  max-reload-search-insns     The maximum number of instructions to search
                              backward when looking for equivalent reload
  max-aliased-vops            The maximum number of virtual operators that a
                              function is allowed to have before triggering
                              memory partitioning heuristics
  avg-aliased-vops            The average number of virtual operators that
                              memory statements are allowed to have before
                              triggering memory partitioning heuristics
  max-sched-region-blocks     The maximum number of blocks in a region to be
                              considered for interblock scheduling
  max-sched-region-insns      The maximum number of insns in a region to be
                              considered for interblock scheduling
  max-pipeline-region-blocks  The maximum number of blocks in a region to be
                              considered for interblock scheduling
  max-pipeline-region-insns   The maximum number of insns in a region to be
                              considered for interblock scheduling
  min-spec-prob               The minimum probability of reaching a source
                              block for interblock speculative scheduling
  max-sched-extend-regions-iters The maximum number of iterations through CFG
                              to extend regions
  max-sched-insn-conflict-delay The maximum conflict delay for an insn to be
                              considered for speculative motion
  sched-spec-prob-cutoff      The minimal probability of speculation success
                              (in percents), so that speculative insn will be
                              scheduled.
  selsched-max-lookahead      The maximum size of the lookahead window of
                              selective scheduling
  selsched-max-sched-times    Maximum number of times that an insn could be
                              scheduled
  selsched-insns-to-rename    Maximum number of instructions in the ready list
                              that are considered eligible for renaming
  sched-mem-true-dep-cost     Minimal distance between possibly conflicting
                              store and load
  max-last-value-rtl          The maximum number of RTL nodes that can be
                              recorded as combiner's last value
  integer-share-limit         The upper bound for sharing integer constants
  min-virtual-mappings        Minimum number of virtual mappings to consider
                              switching to full virtual renames
  virtual-mappings-ratio      Ratio between virtual mappings and virtual
                              symbols to do full virtual renames
  ssp-buffer-size             The lower bound for a buffer to be considered for
                              stack smashing protection
  max-jump-thread-duplication-stmts Maximum number of statements allowed in a
                              block that needs to be duplicated when threading
                              jumps
  max-fields-for-field-sensitive Maximum number of fields in a structure before
                              pointer analysis treats the structure as a single
                              variable
  max-sched-ready-insns       The maximum number of instructions ready to be
                              issued to be considered by the scheduler during
                              the first scheduling pass
  prefetch-latency            The number of insns executed before prefetch is
                              completed
  simultaneous-prefetches     The number of prefetches that can run at the same
                              time
  l1-cache-size               The size of L1 cache
  l1-cache-line-size          The size of L1 cache line
  l2-cache-size               The size of L2 cache
  use-canonical-types         Whether to use canonical types
  max-partial-antic-length    Maximum length of partial antic set when
                              performing tree pre optimization
  sccvn-max-scc-size          Maximum size of a SCC before SCCVN stops
                              processing a function
  ira-max-loops-num           max loops number for regional RA
  ira-max-conflict-table-size max size of conflict table in MB
  switch-conversion-max-branch-ratio The maximum ratio between array size and
                              switch branches for a switch conversion to take
                              place
  loop-invariant-max-bbs-in-loop max basic blocks number in loop for loop
                              invariant motion

The following options control compiler warning messages:
  -Waggregate-return          Warn about returning structures, unions or arrays
  -Warray-bounds              Warn if an array is accessed out of bounds
  -Wattributes                Warn about inappropriate attribute usage
  -Wcast-align                Warn about pointer casts which increase alignment
  -Wcoverage-mismatch         Warn instead of error in case profiles in
                              -fprofile-use do not match
  -Wdeprecated-declarations   Warn about uses of __attribute__((deprecated))
                              declarations
  -Wdisabled-optimization     Warn when an optimization pass is disabled
  -Wextra                     Print extra (possibly unwanted) warnings
  -Winline                    Warn when an inlined function cannot be inlined
  -Wlarger-than-              
  -Wlarger-than=<number>      Warn if an object is larger than <number> bytes
  -Wlogical-op                Warn when a logical operator is suspicously
                              always evaluating to true or false
  -Wmissing-noreturn          Warn about functions which might be candidates
                              for __attribute__((noreturn))
  -Wmudflap                   Warn about constructs not instrumented by
                              -fmudflap
  -Woverflow                  Warn about overflow in arithmetic expressions
  -Wpacked                    Warn when the packed attribute has no effect on
                              struct layout
  -Wpadded                    Warn when padding is required to align structure
                              members
  -Wshadow                    Warn when one local variable shadows another
  -Wstack-protector           Warn when not issuing stack smashing protection
                              for some reason
  -Wstrict-aliasing           Warn about code which might break strict aliasing
                              rules
  -Wstrict-aliasing=          Warn about code which might break strict aliasing
                              rules
  -Wstrict-overflow           Warn about optimizations that assume that signed
                              overflow is undefined
  -Wstrict-overflow=          Warn about optimizations that assume that signed
                              overflow is undefined
  -Wswitch                    Warn about enumerated switches, with no default,
                              missing a case
  -Wswitch-default            Warn about enumerated switches missing a
                              "default:" statement
  -Wswitch-enum               Warn about all enumerated switches missing a
                              specific case
  -Wtype-limits               Warn if a comparison is always true or always
                              false due to the limited range of the data type
  -Wuninitialized             Warn about uninitialized automatic variables
  -Wunreachable-code          Warn about code that will never be executed
  -Wunsafe-loop-optimizations Warn if the loop cannot be optimized due to
                              nontrivial assumptions.
  -Wunused-function           Warn when a function is unused
  -Wunused-parameter          Warn when a function parameter is unused
  -Wunused-value              Warn when an expression value is unused
  -Wunused-variable           Warn when a variable is unused

The following options control optimizations:
  -O<number>                  Set optimization level to <number>
  -Os                         Optimize for space rather than speed
  -falign-functions           Align the start of functions
  -falign-jumps               Align labels which are only reached by jumping
  -falign-labels              Align all labels
  -falign-loops               Align the start of loops
  -fargument-alias            Specify that arguments may alias each other and
                              globals
  -fargument-noalias          Assume arguments may alias globals but not each
                              other
  -fargument-noalias-anything Assume arguments alias no other storage
  -fargument-noalias-global   Assume arguments alias neither each other nor
                              globals
  -fasynchronous-unwind-tables Generate unwind tables that are exact at each
                              instruction boundary
  -fbranch-count-reg          Replace add, compare, branch with branch on count
                              register
  -fbranch-probabilities      Use profiling information for branch probabilities
  -fbranch-target-load-optimize Perform branch target load optimization before
                              prologue / epilogue threading
  -fbranch-target-load-optimize2 Perform branch target load optimization after
                              prologue / epilogue threading
  -fbtr-bb-exclusive          Restrict target load migration not to re-use
                              registers in any basic block
  -fcaller-saves              Save registers around function calls
  -fcommon                    Do not put uninitialized globals in the common
                              section
  -fconserve-stack            Do not perform optimizations increasing
                              noticeably stack usage
  -fcprop-registers           Perform a register copy-propagation optimization
                              pass
  -fcrossjumping              Perform cross-jumping optimization
  -fcse-follow-jumps          When running CSE, follow jumps to their targets
  -fcse-skip-blocks           When running CSE, follow conditional jumps
  -fcx-fortran-rules          Complex multiplication and division follow
                              Fortran rules
  -fcx-limited-range          Omit range reduction step when performing complex
                              division
  -fdata-sections             Place data items into their own section
  -fdce                       Use the RTL dead code elimination pass
  -fdefer-pop                 Defer popping functions args from stack until
                              later
  -fdelayed-branch            Attempt to fill delay slots of branch instructions
  -fdelete-null-pointer-checks Delete useless null pointer checks
  -fdse                       Use the RTL dead store elimination pass
  -fearly-inlining            Perform early inlining
  -fexceptions                Enable exception handling
  -fexpensive-optimizations   Perform a number of minor, expensive optimizations
  -ffinite-math-only          Assume no NaNs or infinities are generated
  -ffloat-store               Don't allocate floats and doubles in extended-
                              precision registers
  -fforward-propagate         Perform a forward propagation pass on RTL
  -fgcse                      Perform global common subexpression elimination
  -fgcse-after-reload         Perform global common subexpression elimination
                              after register allocation has finished
  -fgcse-las                  Perform redundant load after store elimination in
                              global common subexpression elimination
  -fgcse-lm                   Perform enhanced load motion during global common
                              subexpression elimination
  -fgcse-sm                   Perform store motion after global common
                              subexpression elimination
  -fgraphite-identity         Enable Graphite Identity transformation
  -fguess-branch-probability  Enable guessing of branch probabilities
  -fif-conversion             Perform conversion of conditional jumps to
                              branchless equivalents
  -fif-conversion2            Perform conversion of conditional jumps to
                              conditional execution
  -finline-functions-called-once Integrate functions called once into their
                              callers
  -finline-small-functions    Integrate simple functions into their callers
                              when code size is known to not growth
  -fipa-cp                    Perform Interprocedural constant propagation
  -fipa-cp-clone              Perform cloning to make Interprocedural constant
                              propagation stronger
  -fipa-matrix-reorg          Perform matrix layout flattening and transposing
                              based on profiling information.
  -fipa-pta                   Perform interprocedural points-to analysis
  -fipa-pure-const            Discover pure and const functions
  -fipa-reference             Discover readonly and non addressable static
                              variables
  -fipa-type-escape           Type based escape and alias analysis
  -fivopts                    Optimize induction variables on trees
  -fjump-tables               Use jump tables for sufficiently large switch
                              statements
  -floop-block                Enable Loop Blocking transformation
  -floop-interchange          Enable Loop Interchange transformation
  -floop-strip-mine           Enable Loop Strip Mining transformation
  -fmath-errno                Set errno after built-in math functions
  -fmerge-all-constants       Attempt to merge identical constants and constant
                              variables
  -fmerge-constants           Attempt to merge identical constants across
                              compilation units
  -fmodulo-sched              Perform SMS based modulo scheduling before the
                              first scheduling pass
  -fmove-loop-invariants      Move loop invariant computations out of loops
  -fnon-call-exceptions       Support synchronous non-call exceptions
  -fomit-frame-pointer        When possible do not generate stack frames
  -foptimize-register-move    Do the full register move optimization pass
  -foptimize-sibling-calls    Optimize sibling and tail recursive calls
  -fpack-struct               Pack structure members together without holes
  -fpack-struct=<number>      Set initial maximum structure member alignment
  -fpeel-loops                Perform loop peeling
  -fpeephole                  Enable machine specific peephole optimizations
  -fpeephole2                 Enable an RTL peephole pass before sched2
  -fpredictive-commoning      Run predictive commoning optimization.
  -fprefetch-loop-arrays      Generate prefetch instructions, if available, for
                              arrays in loops
  -fpromote-loop-indices      Promote loop indices to word-sized indices when
                              safe
  -freg-struct-return         Return small aggregates in registers
  -fregmove                   Enables a register move optimization
  -frename-registers          Perform a register renaming optimization pass
  -freorder-blocks            Reorder basic blocks to improve code placement
  -freorder-blocks-and-partition Reorder basic blocks and partition into hot
                              and cold sections
  -freorder-functions         Reorder functions to improve code placement
  -frerun-cse-after-loop      Add a common subexpression elimination pass after
                              loop optimizations
  -freschedule-modulo-scheduled-loops Enable/Disable the traditional scheduling
                              in loops that already passed modulo scheduling
  -frounding-math             Disable optimizations that assume default FP
                              rounding behavior
  -frtl-abstract-sequences    Perform sequence abstraction optimization on RTL
  -fsched-interblock          Enable scheduling across basic blocks
  -fsched-spec                Allow speculative motion of non-loads
  -fsched-spec-load           Allow speculative motion of some loads
  -fsched-spec-load-dangerous Allow speculative motion of more loads
  -fsched-stalled-insns       Allow premature scheduling of queued insns
  -fsched-stalled-insns-dep   Set dependence distance checking in premature
                              scheduling of queued insns
  -fsched2-use-superblocks    If scheduling post reload, do superblock
                              scheduling
  -fsched2-use-traces         If scheduling post reload, do trace scheduling
  -fschedule-insns            Reschedule instructions before register allocation
  -fschedule-insns2           Reschedule instructions after register allocation
  -fsection-anchors           Access data in the same section from shared
                              anchor points
  -fsel-sched-pipelining      Perform software pipelining of inner loops during
                              selective scheduling
  -fsel-sched-pipelining-outer-loops Perform software pipelining of outer loops
                              during selective scheduling
  -fsel-sched-reschedule-pipelined Reschedule pipelined regions without
                              pipelining
  -fselective-scheduling      Schedule instructions using selective scheduling
                              algorithm
  -fselective-scheduling2     Run selective scheduling after reload
  -fsignaling-nans            Disable optimizations observable by IEEE
                              signaling NaNs
  -fsigned-zeros              Disable floating point optimizations that ignore
                              the IEEE signedness of zero
  -fsingle-precision-constant Convert floating point constants to single
                              precision constants
  -fsplit-ivs-in-unroller     Split lifetimes of induction variables when loops
                              are unrolled
  -fsplit-wide-types          Split wide types into independent registers
  -fstrict-aliasing           Assume strict aliasing rules apply
  -fthread-jumps              Perform jump threading optimizations
  -ftoplevel-reorder          Reorder top level functions, variables, and asms
  -ftrapping-math             Assume floating-point operations can trap
  -ftrapv                     Trap for signed overflow in addition, subtraction
                              and multiplication
  -ftree-builtin-call-dce     Enable conditional dead code elimination for
                              builtin calls
  -ftree-ccp                  Enable SSA-CCP optimization on trees
  -ftree-ch                   Enable loop header copying on trees
  -ftree-copy-prop            Enable copy propagation on trees
  -ftree-copyrename           Replace SSA temporaries with better names in
                              copies
  -ftree-cselim               Transform condition stores into unconditional ones
  -ftree-dce                  Enable SSA dead code elimination optimization on
                              trees
  -ftree-dominator-opts       Enable dominator optimizations
  -ftree-dse                  Enable dead store elimination
  -ftree-fre                  Enable Full Redundancy Elimination (FRE) on trees
  -ftree-loop-distribution    Enable loop distribution on trees
  -ftree-loop-im              Enable loop invariant motion on trees
  -ftree-loop-ivcanon         Create canonical induction variables in loops
  -ftree-loop-linear          Enable linear loop transforms on trees
  -ftree-loop-optimize        Enable loop optimizations on tree level
  -ftree-lrs                  Perform live range splitting during the SSA-
                              >normal pass
  -ftree-pre                  Enable SSA-PRE optimization on trees
  -ftree-pre-partial-partial  In SSA-PRE optimization on trees, enable partial-
                              partial redundancy elimination.
  -ftree-pre-partial-partial-obliviously In SSA-PRE optimization on trees,
                              enable partial-partial redundancy elimination
                              without regard for the cost of the inserted phi
                              nodes.
  -ftree-reassoc              Enable reassociation on tree level
  -ftree-scev-cprop           Enable copy propagation of scalar-evolution
                              information.
  -ftree-sink                 Enable SSA code sinking on trees
  -ftree-sra                  Perform scalar replacement of aggregates
  -ftree-switch-conversion    Perform conversions of switch initializations.
  -ftree-ter                  Replace temporary expressions in the SSA->normal
                              pass
  -ftree-vect-loop-version    Enable loop versioning when doing loop
                              vectorization on trees
  -ftree-vectorize            Enable loop vectorization on trees
  -ftree-vrp                  Perform Value Range Propagation on trees
  -funit-at-a-time            Compile whole compilation unit at a time
  -funroll-all-loops          Perform loop unrolling for all loops
  -funroll-loops              Perform loop unrolling when iteration count is
                              known
  -funsafe-loop-optimizations Allow loop optimizations to assume that the loops
                              behave in normal way
  -funsafe-math-optimizations Allow math optimizations that may violate IEEE or
                              ISO standards
  -funswitch-loops            Perform loop unswitching
  -funwind-tables             Just generate unwind tables for exception handling
  -fvar-tracking              Perform variable tracking
  -fvar-tracking-uninit       Perform variable tracking and also tag variables
                              that are uninitialized
  -fvariable-expansion-in-unroller Apply variable expansion when loops are
                              unrolled
  -fvect-cost-model           Enable use of cost model in vectorization
  -fvpt                       Use expression value profiles in optimizations
  -fweb                       Construct webs and split unrelated uses of single
                              variable
  -fwhole-program             Perform whole program optimizations
  -fwrapv                     Assume signed arithmetic overflow wraps around

The following options are target specific:
  -falign-arrays              Set the minimum alignment for array variables to
                              be the largest power of two less than or equal to
                              their total storage size, or the biggest
                              alignment used on the machine, whichever is
                              smaller.
  -mabi=                      Specify an ABI
  -mabort-on-noreturn         Generate a call to abort if a noreturn function
                              returns
  -mandroid                   Generate code for the Android operating system.
  -mapcs                      
  -mapcs-float                Pass FP arguments in FP registers
  -mapcs-frame                Generate APCS conformant stack frames
  -mapcs-reentrant            Generate re-entrant, PIC code
  -mapcs-stack-check          
  -march=                     Specify the name of the target architecture
  -marm                       
  -mbig-endian                Assume target CPU is configured as big endian
  -mcallee-super-interworking Thumb: Assume non-static functions may be called
                              from ARM code
  -mcaller-super-interworking Thumb: Assume function pointers may go to non-
                              Thumb aware code
  -mcirrus-fix-invalid-insns  Cirrus: Place NOPs to avoid invalid instruction
                              combinations
  -mcpu=                      Specify the name of the target CPU
  -mfix-cortex-m3-ldrd        Avoid overlapping destination and address
                              registers on LDRD instructions that may trigger
                              Cortex-M3 errata.
  -mfix-janus-2cc             Work around hardware errata for Avalent Janus 2CC
                              cores.
  -mfloat-abi=                Specify if floating point hardware should be used
  -mfp16-format=              Specify the __fp16 floating-point format
  -mfp=                       
  -mfpe                       
  -mfpe=                      
  -mfpu=                      Specify the name of the target floating point
                              hardware/format
  -mhard-float                Alias for -mfloat-abi=hard
  -mlittle-endian             Assume target CPU is configured as little endian
  -mlong-calls                Generate call insns as indirect calls, if
                              necessary
  -mlow-irq-latency           Try to reduce interrupt latency of the generated
                              code
  -mmarvell-div               Generate hardware integer division instructions
                              supported by some Marvell cores.
  -mpic-register=             Specify the register to be used for PIC addressing
  -mpoke-function-name        Store function names in object code
  -msched-prolog              Permit scheduling of a function's prologue
                              sequence
  -msingle-pic-base           Do not load the PIC register in function prologues
  -msoft-float                Alias for -mfloat-abi=soft
  -mstructure-size-boundary=  Specify the minimum bit alignment of structures
  -mthumb                     Compile for the Thumb not the ARM
  -mthumb-interwork           Support calls between Thumb and ARM instruction
                              sets
  -mtp=                       Specify how to access the thread pointer
  -mtpcs-frame                Thumb: Generate (non-leaf) stack frames even if
                              not needed
  -mtpcs-leaf-frame           Thumb: Generate (leaf) stack frames even if not
                              needed
  -mtune=                     Tune code for the given processor
  -mvectorize-with-neon-quad  Use Neon quad-word (rather than double-word)
                              registers for vectorization
  -mword-relocations          Only generate absolute relocations on word sized
                              values.
  -mwords-little-endian       Assume big endian bytes, little endian words

The following options are language-independent:
  --help                      Display this information
  --help=<class>              Display descriptions of a specific class of
                              options.  <class> is one or more of optimizers,
                              target, warnings, undocumented, params
  --param <param>=<value>     Set parameter <param> to value.  See below for a
                              complete list of parameters
  --target-help               Alias for --help=target
  --version                   
  -G<number>                  Put global and static data smaller than <number>
                              bytes into a special section (on some targets)
  -W                          This switch is deprecated; use -Wextra instead
  -Werror=                    Treat specified warning as error
  -Wfatal-errors              Exit on the first error occurred
  -Wframe-larger-than=        -Wframe-larger-than=<number> Warn if a function's
                              stack frame requires more than <number> bytes
  -Wpoison-system-directories Warn for -I and -L options using system
                              directories if cross compiling
  -aux-info <file>            Emit declaration information into <file>
  -aux-info=                  
  -auxbase                    
  -auxbase-strip              
  -dumpbase <file>            Set the file basename to be used for dumps
  -fPIC                       Generate position-independent code if possible
                              (large mode)
  -fPIE                       Generate position-independent code for
                              executables if possible (large mode)
  -fabi-version=              
  -falign-functions=          
  -falign-jumps=              
  -falign-labels=             
  -falign-loops=              
  -fassociative-math          Allow optimization for floating-point arithmetic
                              which may change the result of the operation due
                              to rounding.
  -fauto-inc-dec              Generate auto-inc/dec instructions
  -fbounds-check              Generate code to check bounds before indexing
                              arrays
  -fcall-saved-<register>     Mark <register> as being preserved across
                              functions
  -fcall-used-<register>      Mark <register> as being corrupted by function
                              calls
  -fcheck-data-deps           Compare the results of several data dependence
                              analyzers.
  -fdbg-cnt-list              List all available debugging counters with their
                              limits and counts.
  -fdbg-cnt=                  -fdbg-
                              cnt=<counter>:<limit>[,<counter>:<limit>,...]   
                              Set the debug counter limit.   
  -fdebug-prefix-map=         Map one directory name to another in debug
                              information
  -fdiagnostics-show-location=[once|every-line] How often to emit source
                              location at the beginning of line-wrapped
                              diagnostics
  -fdiagnostics-show-option   Amend appropriate diagnostic messages with the
                              command line option that controls them
  -fdump-<type>               Dump various compiler internals to a file
  -fdump-noaddr               Suppress output of addresses in debugging dumps
  -fdump-unnumbered           Suppress output of instruction numbers, line
                              number notes and addresses in debugging dumps
  -fdwarf2-cfi-asm            Enable CFI tables via GAS assembler directives.
  -feglibc=                   EGLIBC configuration specifier, serves multilib
                              purposes.
  -feliminate-dwarf2-dups     Perform DWARF2 duplicate elimination
  -feliminate-unused-debug-symbols Perform unused type elimination in debug info
  -femit-class-debug-always   Do not suppress C++ class debug information.
  -ffast-math                 
  -ffixed-<register>          Mark <register> as being unavailable to the
                              compiler
  -fforce-addr                Does nothing.  Preserved for backward
                              compatibility.
  -ffunction-cse              Allow function addresses to be held in registers
  -ffunction-sections         Place each function into its own section
  -fgraphite                  Enable in and out of Graphite representation
  -fhelp                      
  -fhelp=                     
  -fident                     Process #ident directives
  -findirect-inlining         Perform indirect inlining
  -finhibit-size-directive    Do not generate .size directives
  -finline                    Pay attention to the "inline" keyword
  -finline-limit-             
  -finline-limit=<number>     Limit the size of inlined functions to <number>
  -finstrument-functions      Instrument function entry and exit with profiling
                              calls
  -finstrument-functions-exclude-file-list= -finstrument-functions-exclude-file-
                              list=filename,...  Do not instrument functions
                              listed in files
  -finstrument-functions-exclude-function-list= -finstrument-functions-exclude-
                              function-list=name,...  Do not instrument listed
                              functions
  -fipa-struct-reorg          Perform structure layout optimizations based on
                              profiling information.
  -fira-algorithm=            -fira-algorithm=[CB|priority] Set the used IRA
                              algorithm
  -fira-coalesce              Do optimistic coalescing.
  -fira-region=               -fira-region=[one|all|mixed] Set regions for IRA
  -fira-share-save-slots      Share slots for saving different hard registers.
  -fira-share-spill-slots     Share stack slots for spilled pseudo-registers.
  -fira-verbose=              -fira-verbose=<number> Control IRA's level of
                              diagnostic messages.
  -fkeep-inline-functions     Generate code for functions even if they are
                              fully inlined
  -fkeep-static-consts        Emit static const variables even if they are not
                              used
  -fleading-underscore        Give external symbols a leading underscore
  -floop-optimize             Does nothing.  Preserved for backward
                              compatibility.
  -fmem-report                Report on permanent memory allocation
  -fmerge-debug-strings       Attempt to merge identical debug strings across
                              compilation units
  -fmessage-length=<number>   Limit diagnostics to <number> characters per
                              line.  0 suppresses line-wrapping
  -fmodulo-sched-allow-regmoves Perform SMS based modulo scheduling with
                              register moves allowed
  -fmudflap                   Add mudflap bounds-checking instrumentation for
                              single-threaded program
  -fmudflapir                 Ignore read operations when inserting mudflap
                              instrumentation
  -fmudflapth                 Add mudflap bounds-checking instrumentation for
                              multi-threaded program
  -fpcc-struct-return         Return small aggregates in memory, not registers
  -fpic                       Generate position-independent code if possible
                              (small mode)
  -fpie                       Generate position-independent code for
                              executables if possible (small mode)
  -fpost-ipa-mem-report       Report on memory allocation before
                              interprocedural optimization
  -fpre-ipa-mem-report        Report on memory allocation before
                              interprocedural optimization
  -fprofile                   Enable basic program profiling code
  -fprofile-arcs              Insert arc-based program profiling code
  -fprofile-correction        Enable correction of flow inconsistent profile
                              data input
  -fprofile-dir=              Set the top-level directory for storing the
                              profile data. The default is 'pwd'.
  -fprofile-generate          Enable common options for generating profile info
                              for profile feedback directed optimizations
  -fprofile-generate=         Enable common options for generating profile info
                              for profile feedback directed optimizations, and
                              set -fprofile-dir=
  -fprofile-use               Enable common options for performing profile
                              feedback directed optimizations
  -fprofile-use=              Enable common options for performing profile
                              feedback directed optimizations, and set
                              -fprofile-dir=
  -fprofile-values            Insert code to profile values of expressions
  -frandom-seed               
  -frandom-seed=<string>      Make compile reproducible using <string>
  -freciprocal-math           Same as -fassociative-math for expressions which
                              include division.
  -frecord-gcc-switches       Record gcc command line switches in the object
                              file.
  -frerun-loop-opt            Does nothing.  Preserved for backward
                              compatibility.
  -fsched-stalled-insns-dep=<number> Set dependence distance checking in
                              premature scheduling of queued insns
  -fsched-stalled-insns=<number> Set number of queued insns that can be
                              prematurely scheduled
  -fsched-verbose=<number>    Set the verbosity level of the scheduler
  -fsee                       Eliminate redundant sign extensions using LCM.
  -fstack-check               Insert stack checking code into the program. 
                              Same as -fstack-check=specific
  -fstack-check=[no|generic|specific] Insert stack checking code into the
                              program
  -fstack-limit               
  -fstack-limit-register=<register> Trap if the stack goes past <register>
  -fstack-limit-symbol=<name> Trap if the stack goes past symbol <name>
  -fstack-protector           Use propolice as a stack protection method
  -fstack-protector-all       Use a stack protection method for every function
  -fstrength-reduce           Does nothing.  Preserved for backward
                              compatibility.
  -fstrict-overflow           Treat signed overflow as undefined
  -fsyntax-only               Check for syntax errors, then stop
  -ftarget-help               
  -ftest-coverage             Create data files needed by "gcov"
  -ftime-report               Report the time taken by each compiler pass
  -ftls-model=[global-dynamic|local-dynamic|initial-exec|local-exec] Set the
                              default thread-local storage code generation model
  -ftracer                    Perform superblock formation via tail duplication
  -ftree-parallelize-loops=   Enable automatic parallelization of loops
  -ftree-salias               Does nothing.  Preserved for backward
                              compatibility.
  -ftree-store-ccp            Does nothing.  Preserved for backward
                              compatibility.
  -ftree-store-copy-prop      Does nothing.  Preserved for backward
                              compatibility.
  -ftree-vectorizer-verbose=<number> Set the verbosity level of the vectorizer
  -fverbose-asm               Add extra commentary to assembler output
  -fvisibility=[default|internal|hidden|protected] Set the default symbol
                              visibility
  -fzero-initialized-in-bss   Put zero initialized data in the bss section
  -g                          Generate debug information in default format
  -gcoff                      Generate debug information in COFF format
  -gdwarf-2                   Generate debug information in DWARF v2 format
  -ggdb                       Generate debug information in default extended
                              format
  -gstabs                     Generate debug information in STABS format
  -gstabs+                    Generate debug information in extended STABS
                              format
  -gvms                       Generate debug information in VMS format
  -gxcoff                     Generate debug information in XCOFF format
  -gxcoff+                    Generate debug information in extended XCOFF
                              format
  -p                          Enable function profiling
  -pie                        Create a position independent executable
  -quiet                      Do not display functions compiled or elapsed time
  -shared                     Create a shared library

COLLECT_GCC_OPTIONS='-v' '-fhelp'

 /opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/../../../../arm-none-eabi/bin/as -v -meabi=5 --help -o /tmp/ccO6fmgn.o /tmp/cccb7VSf.s
GNU assembler version 2.19.51 (arm-none-eabi) using BFD version (Sourcery G++ Lite 2010q1-188) 2.19.51.20090709
Usage: /opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/../../../../arm-none-eabi/bin/as [option...] [asmfile...]
Options:
  -a[sub-option...]	  turn on listings
                      	  Sub-options [default hls]:
                      	  c      omit false conditionals
                      	  d      omit debugging directives
                      	  g      include general info
                      	  h      include high-level source
                      	  l      include assembly
                      	  m      include macro expansions
                      	  n      omit forms processing
                      	  s      include symbols
                      	  =FILE  list to FILE (must be last sub-option)
  --alternate             initially turn on alternate macro syntax
  -D                      produce assembler debugging messages
  --debug-prefix-map OLD=NEW  Map OLD to NEW in debug information
  --defsym SYM=VAL        define symbol SYM to given value
  --execstack             require executable stack for this object
  --noexecstack           don't require executable stack for this object
  -f                      skip whitespace and comment preprocessing
  -g --gen-debug          generate debugging information
  --gstabs                generate STABS debugging information
  --gstabs+               generate STABS debug info with GNU extensions
  --gdwarf-2              generate DWARF2 debugging information
  --hash-size=<value>     set the hash table size close to <value>
  --help                  show this message and exit
  --target-help           show target specific options
  -I DIR                  add DIR to search list for .include directives
  -J                      don't warn about signed overflow
  -K                      warn when differences altered for long displacements
  -L,--keep-locals        keep local symbols (e.g. starting with `L')
  -M,--mri                assemble in MRI compatibility mode
  --MD FILE               write dependency information in FILE (default none)
  -nocpp                  ignored
  -o OBJFILE              name the object-file output OBJFILE (default a.out)
  -R                      fold data section into text section
  --reduce-memory-overheads 
                          prefer smaller memory use at the cost of longer
                          assembly times
  --statistics            print various measured statistics from execution
  --strip-local-absolute  strip local absolute symbols
  --traditional-format    Use same format as native assembler when possible
  --version               print assembler version number and exit
  -W  --no-warn           suppress warnings
  --warn                  don't suppress warnings
  --fatal-warnings        treat warnings as errors
  -w                      ignored
  -X                      ignored
  -Z                      generate object file even after errors
  --listing-lhs-width     set the width in words of the output data column of
                          the listing
  --listing-lhs-width2    set the width in words of the continuation lines
                          of the output data column; ignored if smaller than
                          the width of the first line
  --listing-rhs-width     set the max width in characters of the lines from
                          the source file
  --listing-cont-lines    set the maximum number of continuation lines used
                          for the output data column of the listing
  @FILE                   read options from FILE
 ARM-specific assembler options:
  -k                      generate PIC code
  -mthumb                 assemble Thumb code
  -mthumb-interwork       support ARM/Thumb interworking
  -mapcs-32               code uses 32-bit program counter
  -mapcs-26               code uses 26-bit program counter
  -mapcs-float            floating point args are in fp regs
  -mapcs-reentrant        re-entrant code
  -matpcs                 code is ATPCS conformant
  -mbig-endian            assemble for big-endian
  -mlittle-endian         assemble for little-endian
  -mapcs-frame            use frame pointer
  -mapcs-stack-check      use stack size checking
  -mno-warn-deprecated    do not warn on use of deprecated feature
  -mcpu=<cpu name>	  assemble for CPU <cpu name>
  -march=<arch name>	  assemble for architecture <arch name>
  -mfpu=<fpu name>	  assemble for FPU architecture <fpu name>
  -mfloat-abi=<abi>	  assemble for floating point ABI <abi>
  -meabi=<ver>		  assemble for eabi version <ver>
  -mimplicit-it=<mode>	  controls implicit insertion of IT instructions
  -EB                     assemble code for a big-endian cpu
  -EL                     assemble code for a little-endian cpu
  --fix-v4bx              Allow BX in ARMv4 code

Report bugs to <https://support.codesourcery.com/GNUToolchain/>
COMPILER_PATH=/opt/CodeSourcery/Sourcery_G++_Lite/bin/../libexec/gcc/arm-none-eabi/4.4.1/:/opt/CodeSourcery/Sourcery_G++_Lite/bin/../libexec/gcc/:/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/../../../../arm-none-eabi/bin/
LIBRARY_PATH=/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/:/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/:/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/../../../../arm-none-eabi/lib/:/opt/CodeSourcery/Sourcery_G++_Lite/bin/../arm-none-eabi/lib/
COLLECT_GCC_OPTIONS='-v' '-fhelp'

 /opt/CodeSourcery/Sourcery_G++_Lite/bin/../libexec/gcc/arm-none-eabi/4.4.1/collect2 --sysroot=/opt/CodeSourcery/Sourcery_G++_Lite/bin/../arm-none-eabi -X --help /opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/crti.o /opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/crtbegin.o -L/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1 -L/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc -L/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/../../../../arm-none-eabi/lib -L/opt/CodeSourcery/Sourcery_G++_Lite/bin/../arm-none-eabi/lib /tmp/ccO6fmgn.o --start-group -lgcc -lc --end-group /opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/crtend.o /opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/crtn.o
Usage: /opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/../../../../arm-none-eabi/bin/ld [options] file...
Options:
  -a KEYWORD                  Shared library control for HP/UX compatibility
  -A ARCH, --architecture ARCH
                              Set architecture
  -b TARGET, --format TARGET  Specify target for following input files
  -c FILE, --mri-script FILE  Read MRI format linker script
  -d, -dc, -dp                Force common symbols to be defined
  -e ADDRESS, --entry ADDRESS Set start address
  -E, --export-dynamic        Export all dynamic symbols
  --no-export-dynamic         Undo the effect of --export-dynamic
  -EB                         Link big-endian objects
  -EL                         Link little-endian objects
  -f SHLIB, --auxiliary SHLIB Auxiliary filter for shared object symbol table
  -F SHLIB, --filter SHLIB    Filter for shared object symbol table
  -g                          Ignored
  -G SIZE, --gpsize SIZE      Small data size (if no size, same as --shared)
  -h FILENAME, -soname FILENAME
                              Set internal name of shared library
  -I PROGRAM, --dynamic-linker PROGRAM
                              Set PROGRAM as the dynamic linker to use
  -l LIBNAME, --library LIBNAME
                              Search for library LIBNAME
  -L DIRECTORY, --library-path DIRECTORY
                              Add DIRECTORY to library search path
  --sysroot=<DIRECTORY>       Override the default sysroot location
  -m EMULATION                Set emulation
  -M, --print-map             Print map file on standard output
  -n, --nmagic                Do not page align data
  -N, --omagic                Do not page align data, do not make text readonly
  --no-omagic                 Page align data, make text readonly
  -o FILE, --output FILE      Set output file name
  -O                          Optimize output file
  -Qy                         Ignored for SVR4 compatibility
  -q, --emit-relocs           Generate relocations in final output
  -r, -i, --relocatable       Generate relocatable output
  -R FILE, --just-symbols FILE
                              Just link symbols (if directory, same as --rpath)
  -s, --strip-all             Strip all symbols
  -S, --strip-debug           Strip debugging symbols
  --strip-discarded           Strip symbols in discarded sections
  --no-strip-discarded        Do not strip symbols in discarded sections
  -t, --trace                 Trace file opens
  -T FILE, --script FILE      Read linker script
  --default-script FILE, -dT  Read default linker script
  -u SYMBOL, --undefined SYMBOL
                              Start with undefined reference to SYMBOL
  --unique [=SECTION]         Don't merge input [SECTION | orphan] sections
  -Ur                         Build global constructor/destructor tables
  -v, --version               Print version information
  -V                          Print version and emulation information
  -x, --discard-all           Discard all local symbols
  -X, --discard-locals        Discard temporary local symbols (default)
  --discard-none              Don't discard any local symbols
  -y SYMBOL, --trace-symbol SYMBOL
                              Trace mentions of SYMBOL
  -Y PATH                     Default search path for Solaris compatibility
  -(, --start-group           Start a group
  -), --end-group             End a group
  --accept-unknown-input-arch Accept input files whose architecture cannot be determined
  --no-accept-unknown-input-arch
                              Reject input files whose architecture is unknown
  --add-needed                Set DT_NEEDED tags for DT_NEEDED entries in
                                following dynamic libs
  --no-add-needed             Do not set DT_NEEDED tags for DT_NEEDED entries
                                in following dynamic libs
  --as-needed                 Only set DT_NEEDED for following dynamic libs if used
  --no-as-needed              Always set DT_NEEDED for following dynamic libs
  -assert KEYWORD             Ignored for SunOS compatibility
  -Bdynamic, -dy, -call_shared
                              Link against shared libraries
  -Bstatic, -dn, -non_shared, -static
                              Do not link against shared libraries
  -Bsymbolic                  Bind global references locally
  -Bsymbolic-functions        Bind global function references locally
  --check-sections            Check section addresses for overlaps (default)
  --no-check-sections         Do not check section addresses for overlaps
  --cref                      Output cross reference table
  --defsym SYMBOL=EXPRESSION  Define a symbol
  --demangle [=STYLE]         Demangle symbol names [using STYLE]
  --embedded-relocs           Generate embedded relocs
  --fatal-warnings            Treat warnings as errors
  --no-fatal-warnings         Do not treat warnings as errors (default)
  -fini SYMBOL                Call SYMBOL at unload-time
  --force-exe-suffix          Force generation of file with .exe suffix
  --gc-sections               Remove unused sections (on some targets)
  --no-gc-sections            Don't remove unused sections (default)
  --print-gc-sections         List removed unused sections on stderr
  --no-print-gc-sections      Do not list removed unused sections
  --hash-size=<NUMBER>        Set default hash table size close to <NUMBER>
  --help                      Print option help
  -init SYMBOL                Call SYMBOL at load-time
  -Map FILE                   Write a map file
  --no-define-common          Do not define Common storage
  --no-demangle               Do not demangle symbol names
  --no-keep-memory            Use less memory and more disk I/O
  --no-undefined              Do not allow unresolved references in object files
  --allow-shlib-undefined     Allow unresolved references in shared libaries
  --no-allow-shlib-undefined  Do not allow unresolved references in shared libs
  --allow-multiple-definition Allow multiple definitions
  --no-undefined-version      Disallow undefined version
  --default-symver            Create default symbol version
  --default-imported-symver   Create default symbol version for imported symbols
  --no-warn-mismatch          Don't warn about mismatched input files
  --no-warn-search-mismatch   Don't warn on finding an incompatible library
  --no-whole-archive          Turn off --whole-archive
  --noinhibit-exec            Create an output file even if errors occur
  -nostdlib                   Only use library directories specified on
                                the command line
  --oformat TARGET            Specify target of output file
  -qmagic                     Ignored for Linux compatibility
  --reduce-memory-overheads   Reduce memory overheads, possibly taking much longer
  --relax                     Relax branches on certain targets
  --retain-symbols-file FILE  Keep only symbols listed in FILE
  -rpath PATH                 Set runtime shared library search path
  -rpath-link PATH            Set link time shared library search path
  -shared, -Bshareable        Create a shared library
  -pie, --pic-executable      Create a position independent executable
  --sort-common [=ascending|descending]
                              Sort common symbols by alignment [in specified order]
  --sort-section name|alignment
                              Sort sections by name or maximum alignment
  --spare-dynamic-tags COUNT  How many tags to reserve in .dynamic section
  --split-by-file [=SIZE]     Split output sections every SIZE octets
  --split-by-reloc [=COUNT]   Split output sections every COUNT relocs
  --stats                     Print memory usage statistics
  --target-help               Display target specific options
  --task-link SYMBOL          Do task level linking
  --traditional-format        Use same format as native linker
  --section-start SECTION=ADDRESS
                              Set address of named section
  -Tbss ADDRESS               Set address of .bss section
  -Tdata ADDRESS              Set address of .data section
  -Ttext ADDRESS              Set address of .text section
  -Ttext-segment ADDRESS      Set address of text segment
  --unresolved-symbols=<method>
                              How to handle unresolved symbols.  <method> is:
                                ignore-all, report-all, ignore-in-object-files,
                                ignore-in-shared-libs
  --verbose                   Output lots of information during link
  --version-script FILE       Read version information script
  --version-exports-section SYMBOL
                              Take export symbols list from .exports, using
                                SYMBOL as the version.
  --dynamic-list-data         Add data symbols to dynamic list
  --dynamic-list-cpp-new      Use C++ operator new/delete dynamic list
  --dynamic-list-cpp-typeinfo Use C++ typeinfo dynamic list
  --dynamic-list FILE         Read dynamic list
  --warn-common               Warn about duplicate common symbols
  --warn-constructors         Warn if global constructors/destructors are seen
  --warn-multiple-gp          Warn if the multiple GP values are used
  --warn-once                 Warn only once per undefined symbol
  --warn-section-align        Warn if start of section changes due to alignment
  --warn-shared-textrel       Warn if shared object has DT_TEXTREL
  --warn-alternate-em         Warn if an object has alternate ELF machine code
  --warn-unresolved-symbols   Report unresolved symbols as warnings
  --error-unresolved-symbols  Report unresolved symbols as errors
  --whole-archive             Include all objects from following archives
  --wrap SYMBOL               Use wrapper functions for SYMBOL
  --no-poison-system-directories
                              Do not warn for -L options using system directories
  --error-poison-system-directories
                              Give an error for -L options using system directories
  @FILE                       Read options from FILE
/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/../../../../arm-none-eabi/bin/ld: supported targets: elf32-littlearm elf32-bigarm elf32-little elf32-big srec symbolsrec verilog tekhex binary ihex
/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/../../../../arm-none-eabi/bin/ld: supported emulations: armelf
/opt/CodeSourcery/Sourcery_G++_Lite/bin/../lib/gcc/arm-none-eabi/4.4.1/../../../../arm-none-eabi/bin/ld: emulation specific options:
armelf: 
  --build-id[=STYLE]          Generate build ID note
  -Bgroup                     Selects group name lookup rules for DSO
  --disable-new-dtags         Disable new dynamic tags
  --enable-new-dtags          Enable new dynamic tags
  --eh-frame-hdr              Create .eh_frame_hdr section
  --hash-style=STYLE          Set hash style to sysv, gnu or both
  -z combreloc                Merge dynamic relocs into one section and sort
  -z defs                     Report unresolved symbols in object files.
  -z execstack                Mark executable as requiring executable stack
  -z initfirst                Mark DSO to be initialized first at runtime
  -z interpose                Mark object to interpose all DSOs but executable
  -z lazy                     Mark object lazy runtime binding (default)
  -z loadfltr                 Mark object requiring immediate process
  -z muldefs                  Allow multiple definitions
  -z nocombreloc              Don't merge dynamic relocs into one section
  -z nocopyreloc              Don't create copy relocs
  -z nodefaultlib             Mark object not to use default search paths
  -z nodelete                 Mark DSO non-deletable at runtime
  -z nodlopen                 Mark DSO not available to dlopen
  -z nodump                   Mark DSO not available to dldump
  -z noexecstack              Mark executable as not requiring executable stack
  -z now                      Mark object non-lazy runtime binding
  -z origin                   Mark object requiring immediate $ORIGIN
                                processing at runtime
  -z max-page-size=SIZE       Set maximum page size to SIZE
  -z common-page-size=SIZE    Set common page size to SIZE
  -z KEYWORD                  Ignored for Solaris compatibility
  --thumb-entry=<sym>         Set the entry point to be Thumb symbol <sym>
  --be8                       Output BE8 format image
  --target1=rel               Interpret R_ARM_TARGET1 as R_ARM_REL32
  --target1=abs               Interpret R_ARM_TARGET1 as R_ARM_ABS32
  --target2=<type>            Specify definition of R_ARM_TARGET2
  --fix-v4bx                  Rewrite BX rn as MOV pc, rn for ARMv4
  --fix-v4bx-interworking     Rewrite BX rn branch to ARMv4 interworking veneer
  --use-blx                   Enable use of BLX instructions
  --vfp11-denorm-fix          Specify how to fix VFP11 denorm erratum
  --no-enum-size-warning      Don't warn about objects with incompatible
                                enum sizes
  --no-wchar-size-warning     Don't warn about objects with incompatible                                wchar_t sizes
  --pic-veneer                Always generate PIC interworking veneers
   --stub-group-size=N   Maximum size of a group of input sections that can be
                           handled by one stub section.  A negative value
                           locates all stubs after their branches (with a
                           group size of -N), while a positive value allows
                           two groups of input sections, one before, and one
                           after each stub section.  Values of +/-1 indicate
                           the linker should choose suitable defaults.
  --[no-]fix-cortex-a8        Disable/enable Cortex-A8 Thumb-2 branch erratum fix

Report bugs to <https://support.codesourcery.com/GNUToolchain/>

For bug reporting instructions, please see:
<https://support.codesourcery.com/GNUToolchain/>
