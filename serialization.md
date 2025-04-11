<div class="learn__post__content">
        

        <div>
  
</div>


        <h1 id="serialization">Serialization</h1>

<div class="bootstrap">
    <div class="plans-blockquote bg-blue-95 rounded-3 p-6 d-flex flex-row border border-1 border-primary">
        <svg class="" width="24" height="24" viewBox="0 0 26 26" fill="none">
  <path d="M12 13V15" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke="#509EE3"></path>
  <path d="M12 10C12.5523 10 13 9.55228 13 9C13 8.44772 12.5523 8 12 8C11.4477 8 11 8.44772 11 9C11 9.55228 11.4477 10 12 10Z" fill="#509EE3"></path>
  <path d="M12 19.25C16.0041 19.25 19.25 16.0041 19.25 12C19.25 7.99594 16.0041 4.75 12 4.75C7.99594 4.75 4.75 7.99594 4.75 12C4.75 16.0041 7.99594 19.25 12 19.25Z" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" stroke="#509EE3"></path>
</svg>

        
       <p class="m-0 ms-2 paragraph-5 neutral-40">Serialization is only available on <a class="fw-bold" href="/product/pro">Pro</a> and <a class="fw-bold link-purple" href="/product/enterprise">Enterprise</a> plans
        
        (both self-hosted and on Metabase Cloud).
        </p>
    </div>
</div>

<p>Once you really get rolling with Metabase, it’s often the case that you’ll have more than one Metabase instance spun up. You might have a couple of testing or development instances and a few production ones, or maybe you have a separate Metabase per office or region.</p>

<p>To help you out in situations like this, Metabase has a serialization feature which lets you create an <em>export</em> of the contents of a Metabase that can then be <em>imported</em> into one or more Metabases.</p>

<p><strong>Export</strong> will serialize the contents of your source Metabase as YAML files.</p>

<p><strong>Import</strong> will read those exported YAML files and create or update items in the target Metabase based on the contents serialized in those YAML files.</p>

<p>There are two ways to run these <code class="language-plaintext highlighter-rouge">export</code> and <code class="language-plaintext highlighter-rouge">import</code> commands:</p>

<ul>
  <li><a href="#serialization-with-cli-commands">Using CLI commands</a></li>
  <li><a href="#serialization-via-the-api">Through the API</a>.</li>
</ul>

<blockquote>
  <p>We’re interested in how we can improve serialization to suit your workflow. <a href="https://github.com/metabase/metabase/issues?q=is%3Aissue+is%3Aopen+serialization+label%3AOperation%2FSerialization">Upvote an existing issue</a> to let us know it’s important to you. If a relevant issue doesn’t yet exist, please create one and tell us what you need.</p>
</blockquote>

<div class="copy-clip-container h2"><h2 id="serialization-use-cases">Serialization use cases</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<ul>
  <li><strong>Staging environments</strong>. Enable a staging-to-production workflow for important dashboards by exporting from a staging instance of Metabase and then importing them into your production instance(s).</li>
  <li><strong>Version control</strong>. Check the exported files into version control and audit changes to them, as the YAML files contained within the export are pretty readable.</li>
  <li><strong>Duplicating assets to other Metabase instances</strong>. Export the “template” data from a source Metabase and import them to one or more target instances.</li>
</ul>

<p>Check out our guides for:</p>

<ul>
  <li><a href="/learn/metabase-basics/administration/administration-and-operation/multi-env">Running multiple environments</a></li>
  <li><a href="/learn/metabase-basics/administration/administration-and-operation/git-based-workflow">Setting up git-based workflow</a></li>
</ul>

<blockquote>
  <p>Serialization isn’t intended for use cases like duplicating assets or swapping data sources <em>within</em> the same Metabase instance. If you’re using serialization for duplicating assets within the same instance, check out <a href="#how-export-works">How export works</a>, <a href="#how-import-works">How import works</a>, and the directions for your use case in <a href="#other-uses-of-serialization">Other uses of serialization</a></p>
</blockquote>

<div class="copy-clip-container h2"><h2 id="how-export-works">How export works</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<ul>
  <li><a href="#what-gets-exported">What gets exported</a></li>
  <li><a href="#general-metabase-settings-that-are-exported">General Metabase settings that get exported</a></li>
  <li><a href="#customize-what-gets-exported">Customize what gets exported</a></li>
  <li><a href="#example-of-a-serialized-question">Example of a serialized question</a></li>
  <li><a href="#metabase-uses-entity-ids-to-identify-and-reference-metabase-items">Metabase uses Entity IDs to identify and reference items</a></li>
</ul>

<div class="copy-clip-container h3"><h3 id="what-gets-exported">What gets exported</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Metabase will only export the following entities:</p>

<ul>
  <li>Collections (but personal collections don’t get exported unless explicitly specified them through <a href="#customize-what-gets-exported">export options</a>)</li>
  <li>Dashboards</li>
  <li>Saved questions</li>
  <li>Actions</li>
  <li>Models</li>
  <li>Metrics</li>
  <li>Snippets</li>
  <li>Data model and table metadata</li>
  <li>Segments</li>
  <li>Public sharing settings for questions and dashboards</li>
  <li><a href="#general-metabase-settings-that-are-exported">General Metabase settings</a></li>
  <li>Events and timelines</li>
  <li>Database connection strings (only if specified through <a href="#customize-what-gets-exported">export options</a>).</li>
</ul>

<p>All other entities—including users, groups, permissions, alerts, subscriptions—won’t get exported.</p>

<p>Metabase will export its artifacts to a directory of YAML files. The export includes:</p>

<ul>
  <li>
    <p>Directories that contain YAML files for various Metabase entities.
An example export could include the following directories, depending on what you exported and the contents of your Metabase:</p>

    <ul>
      <li>actions</li>
      <li>collections
        <ul>
          <li>cards</li>
          <li>dashboards</li>
          <li>timelines</li>
        </ul>
      </li>
      <li>databases</li>
    </ul>

    <p>When serializing through the API, the export directory <a href="#you-must-compress-your-files-when-serializing-via-api-calls">will be a compressed into a .tar.gz file</a>.</p>
  </li>
  <li>
    <p>A <code class="language-plaintext highlighter-rouge">settings.yaml</code> file that includes some <a href="#general-metabase-settings-that-are-exported">Metabase-wide settings</a></p>
  </li>
</ul>

<p>Database connection details are not included by default, so you but you can <a href="#customize-what-gets-exported">configure your export</a> to include them.</p>

<div class="copy-clip-container h3"><h3 id="general-metabase-settings-that-are-exported">General Metabase settings that are exported</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Here’s the list of the general settings Metabase exports in the <code class="language-plaintext highlighter-rouge">settings.yaml</code> file. For more on Metabase settings, see <a href="../configuring-metabase/start">Configuring Metabase</a>.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">humanization-strategy
native-query-autocomplete-match-style
site-locale
report-timezone-short
report-timezone-long
application-name
enable-xrays
show-homepage-pin-message
source-address-header
enable-nested-queries
custom-geojson-enabled
start-of-week
custom-geojson
available-timezones
unaggregated-query-row-limit
aggregated-query-row-limit
hide-embed-branding?
search-typeahead-enabled
enable-sandboxes?
application-font
available-locales
landing-page
enable-embedding
application-colors
application-logo-url
application-favicon-url
show-homepage-xrays
show-metabot
enable-whitelabeling?
show-homepage-data
site-name
application-font-files
loading-message
report-timezone
persisted-models-enabled
enable-content-management?
subscription-allowed-domains
breakout-bins-num
available-fonts
custom-formatting
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="customize-what-gets-exported">Customize what gets exported</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>You can customize what gets exported. You can tell Metabase:</p>

<ul>
  <li>Export specific collections</li>
  <li>Do not export collections</li>
  <li>Do not export Metabase settings</li>
  <li>Do not export table metadata</li>
  <li>Include sample field values (excluded by default)</li>
  <li>Include database connection details (excluded by default)</li>
</ul>

<p>See <a href="#export-options">export parameters in CLI commands</a> or <a href="#api-export-parameters">export parameters in API calls</a>.</p>

<div class="copy-clip-container h3"><h3 id="example-of-a-serialized-question">Example of a serialized question</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Questions can be found in the <code class="language-plaintext highlighter-rouge">cards</code> directory of a collection directory. Here’s an example card YAML file for a question written with SQL that uses a field filter and has an area chart visualization.</p>

<blockquote>
  <p>To preserve a native query’s multi-line format, remove trailing whitespace from native queries. If your native query has trailing whitespace, YAML will convert your query to a single string literal (which only affects presentation, not functionality).</p>
</blockquote>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-yml hljs language-yaml" data-highlighted="yes"><span class="hljs-attr">name:</span> <span class="hljs-string">Products</span> <span class="hljs-string">by</span> <span class="hljs-string">week</span>
<span class="hljs-attr">description:</span> <span class="hljs-string">Area</span> <span class="hljs-string">chart</span> <span class="hljs-string">of</span> <span class="hljs-string">products</span> <span class="hljs-string">created</span> <span class="hljs-string">by</span> <span class="hljs-string">week</span>
<span class="hljs-attr">entity_id:</span> <span class="hljs-string">r6vC_vLmo9zG6_r9sAuYG</span>
<span class="hljs-attr">created_at:</span> <span class="hljs-string">"2024-05-08T19:10:24.348808Z"</span>
<span class="hljs-attr">creator_id:</span> <span class="hljs-string">admin@metabase.local</span>
<span class="hljs-attr">display:</span> <span class="hljs-string">area</span>
<span class="hljs-attr">archived:</span> <span class="hljs-literal">false</span>
<span class="hljs-attr">collection_id:</span> <span class="hljs-string">onou5H28Wvy3kWnjxxdKQ</span>
<span class="hljs-attr">collection_preview:</span> <span class="hljs-literal">true</span>
<span class="hljs-attr">collection_position:</span> <span class="hljs-literal">null</span>
<span class="hljs-attr">query_type:</span> <span class="hljs-string">native</span>
<span class="hljs-attr">dataset:</span> <span class="hljs-literal">false</span>
<span class="hljs-attr">cache_ttl:</span> <span class="hljs-literal">null</span>
<span class="hljs-attr">database_id:</span> <span class="hljs-string">Sample</span> <span class="hljs-string">Database</span>
<span class="hljs-attr">table_id:</span> <span class="hljs-literal">null</span>
<span class="hljs-attr">enable_embedding:</span> <span class="hljs-literal">false</span>
<span class="hljs-attr">embedding_params:</span> <span class="hljs-literal">null</span>
<span class="hljs-attr">made_public_by_id:</span> <span class="hljs-literal">null</span>
<span class="hljs-attr">public_uuid:</span> <span class="hljs-literal">null</span>
<span class="hljs-attr">parameters:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">default:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">Gizmo</span>
    <span class="hljs-attr">id:</span> <span class="hljs-string">c37d2f38-05fa-48c4-a208-19d9dba803c6</span>
    <span class="hljs-attr">name:</span> <span class="hljs-string">Pick</span> <span class="hljs-string">a</span> <span class="hljs-string">category</span>
    <span class="hljs-attr">slug:</span> <span class="hljs-string">category_filter</span>
    <span class="hljs-attr">target:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">dimension</span>
      <span class="hljs-bullet">-</span> <span class="hljs-bullet">-</span> <span class="hljs-string">template-tag</span>
        <span class="hljs-bullet">-</span> <span class="hljs-string">category_filter</span>
    <span class="hljs-attr">type:</span> <span class="hljs-string">string/=</span>
<span class="hljs-attr">parameter_mappings:</span> []
<span class="hljs-attr">dataset_query:</span>
  <span class="hljs-attr">database:</span> <span class="hljs-string">Sample</span> <span class="hljs-string">Database</span>
  <span class="hljs-attr">native:</span>
    <span class="hljs-attr">query:</span> <span class="hljs-string">|-
      SELECT
        category,
        date_trunc ('week', created_at) AS "Week",
        count(*) AS "Count"
      FROM
        products
      WHERE
        
      GROUP BY
        category,
        "Week"
</span>    <span class="hljs-attr">template-tags:</span>
      <span class="hljs-attr">category_filter:</span>
        <span class="hljs-attr">default:</span>
          <span class="hljs-bullet">-</span> <span class="hljs-string">Gizmo</span>
        <span class="hljs-attr">dimension:</span>
          <span class="hljs-bullet">-</span> <span class="hljs-string">field</span>
          <span class="hljs-bullet">-</span> <span class="hljs-bullet">-</span> <span class="hljs-string">Sample</span> <span class="hljs-string">Database</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">PUBLIC</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">PRODUCTS</span>
            <span class="hljs-bullet">-</span> <span class="hljs-string">CATEGORY</span>
          <span class="hljs-bullet">-</span> <span class="hljs-attr">base-type:</span> <span class="hljs-string">type/Text</span>
        <span class="hljs-attr">display-name:</span> <span class="hljs-string">Pick</span> <span class="hljs-string">a</span> <span class="hljs-string">category</span>
        <span class="hljs-attr">id:</span> <span class="hljs-string">c37d2f38-05fa-48c4-a208-19d9dba803c6</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">category_filter</span>
        <span class="hljs-attr">type:</span> <span class="hljs-string">dimension</span>
        <span class="hljs-attr">widget-type:</span> <span class="hljs-string">string/=</span>
  <span class="hljs-attr">type:</span> <span class="hljs-string">native</span>
<span class="hljs-attr">result_metadata:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">base_type:</span> <span class="hljs-string">type/Text</span>
    <span class="hljs-attr">display_name:</span> <span class="hljs-string">CATEGORY</span>
    <span class="hljs-attr">effective_type:</span> <span class="hljs-string">type/Text</span>
    <span class="hljs-attr">field_ref:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">field</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">CATEGORY</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">base-type:</span> <span class="hljs-string">type/Text</span>
    <span class="hljs-attr">name:</span> <span class="hljs-string">CATEGORY</span>
    <span class="hljs-attr">semantic_type:</span> <span class="hljs-literal">null</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">base_type:</span> <span class="hljs-string">type/DateTime</span>
    <span class="hljs-attr">display_name:</span> <span class="hljs-string">Week</span>
    <span class="hljs-attr">effective_type:</span> <span class="hljs-string">type/DateTime</span>
    <span class="hljs-attr">field_ref:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">field</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">Week</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">base-type:</span> <span class="hljs-string">type/DateTime</span>
    <span class="hljs-attr">name:</span> <span class="hljs-string">Week</span>
    <span class="hljs-attr">semantic_type:</span> <span class="hljs-literal">null</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">base_type:</span> <span class="hljs-string">type/BigInteger</span>
    <span class="hljs-attr">display_name:</span> <span class="hljs-string">Count</span>
    <span class="hljs-attr">effective_type:</span> <span class="hljs-string">type/BigInteger</span>
    <span class="hljs-attr">field_ref:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">field</span>
      <span class="hljs-bullet">-</span> <span class="hljs-string">Count</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">base-type:</span> <span class="hljs-string">type/BigInteger</span>
    <span class="hljs-attr">name:</span> <span class="hljs-string">Count</span>
    <span class="hljs-attr">semantic_type:</span> <span class="hljs-string">type/Quantity</span>
<span class="hljs-attr">visualization_settings:</span>
  <span class="hljs-attr">column_settings:</span> <span class="hljs-literal">null</span>
  <span class="hljs-attr">graph.dimensions:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">Week</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">CATEGORY</span>
  <span class="hljs-attr">graph.metrics:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">Count</span>
<span class="hljs-attr">serdes/meta:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">id:</span> <span class="hljs-string">r6vC_vLmo9zG6_r9sAuYG</span>
    <span class="hljs-attr">label:</span> <span class="hljs-string">products_created_by_week</span>
    <span class="hljs-attr">model:</span> <span class="hljs-string">Card</span>
<span class="hljs-attr">initially_published_at:</span> <span class="hljs-literal">null</span>
<span class="hljs-attr">metabase_version:</span> <span class="hljs-string">v1.49.7</span> <span class="hljs-string">(f0ff786)</span>
<span class="hljs-attr">type:</span> <span class="hljs-string">question</span>
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="metabase-uses-entity-ids-to-identify-and-reference-metabase-items">Metabase uses Entity IDs to identify and reference Metabase items</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Metabase assigns a unique Entity ID to every Metabase item (a dashboard, question, model, collection, etc.). These Entity IDs are in addition to the sequential IDs Metabase generates. Entity IDs use the <a href="https://github.com/ai/nanoid">NanoID format</a>, and are stable across Metabases. By “stable” we mean that you can, for example, export a dashboard with an entity ID from one Metabase, and import that dashboard into another Metabase and have that dashboard use the same Entity ID, even though it’s in a different Metabase.</p>

<p>To get an item’s Entity ID in Metabase:</p>

<ol>
  <li>Visit the item in Metabase.</li>
  <li>Click on the info button.</li>
  <li>In the overview tab, copy the Entity ID.</li>
</ol>

<p>You can also see the Entity IDs of items in the exported YAML files in the <code class="language-plaintext highlighter-rouge">entity_id</code> field. For example, in the <a href="#example-of-a-serialized-question">Example of a serialized question</a>, you’ll see the Entity ID of that question:</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-yaml hljs" data-highlighted="yes"><span class="hljs-attr">entity_id:</span> <span class="hljs-string">r6vC_vLmo9zG6_r9sAuYG</span>
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>This ID also appears in the <code class="language-plaintext highlighter-rouge">serdes/meta → id</code> field (these IDs must match):</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-yaml hljs" data-highlighted="yes"><span class="hljs-attr">serdes/meta:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-attr">id:</span> <span class="hljs-string">r6vC_vLmo9zG6_r9sAuYG</span>
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>To disambiguate entities that share the same name, Metabase includes Entity IDs in the file and directory names for exported entities.</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">r6vC_vLmo9zG6_r9sAuYG_products_by_week.yaml
IA96oUzmUbYfNFl0GzhRj_accounts_model.yaml
KUEGiWvoBFEc5oGQCEnPg_converted_customers.yaml
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>For example, in the <a href="#example-of-a-serialized-question">Example of a serialized question</a> above, you can see the field <code class="language-plaintext highlighter-rouge">collection_id</code>:</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-yaml hljs" data-highlighted="yes"><span class="hljs-attr">collection_id:</span> <span class="hljs-string">onou5H28Wvy3kWnjxxdKQ</span>
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>This ID refers to the collection where the question was saved. In a real export, you’d be able to find a YAML file for this collection whose name starts with its ID: <code class="language-plaintext highlighter-rouge">onou5H28Wvy3kWnjxxdKQ</code>.</p>

<div class="copy-clip-container h3"><h3 id="entity-ids-work-with-embedding">Entity IDs work with embedding</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Metabase supports working with <a href="#metabase-uses-entity-ids-to-identify-and-reference-metabase-items">Entity IDs</a> for questions, dashboards, and collections in <a href="../embedding/static-embedding">Static Embedding</a>, <a href="../embedding/interactive-embedding">Interactive embedding</a>, and the <a href="../embedding/sdk/introduction">Embedded Analytics SDK</a>.</p>

<p>A high-level workflow for using Entity IDs when embedding Metabase in your app would look something like:</p>

<ol>
  <li>Create a dashboard in a Metabase running locally on your machine.</li>
  <li>Embed the dashboard in your app locally using the Entity ID in your application code.</li>
  <li>Export your Metabase changes to YAML files via serialization.</li>
  <li>Import your Metabase changes (the exported YAML files) to your production Metabase.</li>
  <li>Since the Entity ID remains the same in the production Metabase, you can just push the code in your app to production, and the code will refer to the right dashboard.</li>
</ol>

<div class="copy-clip-container h3"><h3 id="databases-schemas-tables-and-fields-are-identified-by-name">Databases, schemas, tables, and fields are identified by name</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>By default, Metabase exports some database and data model settings. Exports exclude database connection strings by default. You can <a href="#customize-what-gets-exported">explicitly include database connection strings</a>. You can also choose to exclude the data model entirely.</p>

<p>Metabase serializes databases and tables in the <code class="language-plaintext highlighter-rouge">databases</code> directory. It will include YAML files for every database, table, field, segment, and metric.</p>

<p>Databases, tables, and fields are referred to by their names (unlike Metabase-specific items, which are <a href="#metabase-uses-entity-ids-to-identify-and-reference-metabase-items">referred to by Entity IDs</a>).</p>

<p>For example, in the <a href="#example-of-a-serialized-question">Example of a serialized question</a>, there are several YAML keys that reference Sample Database:</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-yaml hljs" data-highlighted="yes"><span class="hljs-attr">database_id:</span> <span class="hljs-string">Sample</span> <span class="hljs-string">Database</span>
<span class="hljs-meta">---</span>
<span class="hljs-attr">dataset_query:</span>
  <span class="hljs-attr">database:</span> <span class="hljs-string">Sample</span> <span class="hljs-string">Database</span>
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>In the description of the field filter (<code class="language-plaintext highlighter-rouge">category_filter:</code>) in that example, you can see the reference to the field that’s used to populate the filter options:</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-yaml hljs" data-highlighted="yes"><span class="hljs-attr">dimension:</span>
  <span class="hljs-bullet">-</span> <span class="hljs-string">field</span>
  <span class="hljs-bullet">-</span> <span class="hljs-bullet">-</span> <span class="hljs-string">Sample</span> <span class="hljs-string">Database</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">PUBLIC</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">PRODUCTS</span>
    <span class="hljs-bullet">-</span> <span class="hljs-string">CATEGORY</span>
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>It refers to the <code class="language-plaintext highlighter-rouge">CATEGORY</code> field in the <code class="language-plaintext highlighter-rouge">PRODUCTS</code> table in the <code class="language-plaintext highlighter-rouge">PUBLIC</code> schema in <code class="language-plaintext highlighter-rouge">Sample Database</code>. The serialized <code class="language-plaintext highlighter-rouge">Sample Database</code> in the <code class="language-plaintext highlighter-rouge">databases</code> directory will also include YAML files for this field and table.</p>

<div class="copy-clip-container h2"><h2 id="how-import-works">How import works</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>During import, Metabase will read the provided YAML files and create items according to the YAML specs. <a href="#example-of-a-serialized-question">Example of a serialized question</a> how Metabase records information it needs to reconstruct an item.</p>

<p>Metabase will not delete items from target instance during import, but it will overwrite items that already exist.</p>

<p>Metabase relies on <a href="#metabase-uses-entity-ids-to-identify-and-reference-metabase-items">Entity IDs</a> to figure out which items to create or overwrite, and what are the relationships between items. When importing into an instance that already has some content in it, keep in mind:</p>

<ul>
  <li>
    <p>If you import an item with an <code class="language-plaintext highlighter-rouge">entity_id</code> that doesn’t exist in your target Metabase, Metabase will create a new item.</p>
  </li>
  <li>
    <p>If you import an item with an <code class="language-plaintext highlighter-rouge">entity_id</code> that already exists in your target Metabase, the existing item will be overwritten.</p>

    <p>In particular, this means that if you export a question, then make a change in an exported YAML file — like rename a question by directly editing the <code class="language-plaintext highlighter-rouge">name</code> field — and then import the edited file back, Metabase will try to apply the changes you made to the YAML.</p>
  </li>
  <li>
    <p>If you import an item with a blank <code class="language-plaintext highlighter-rouge">entity_id</code>, Metabase will create a new item. Any <code class="language-plaintext highlighter-rouge">serdes/meta → id</code> will be ignored in this case.</p>
  </li>
  <li>
    <p>All items and data sources referenced in YAML must either exist in the target Metabase already, or be included in the import.</p>

    <p>For example, if an exported YAML has the field <code class="language-plaintext highlighter-rouge">collection_id: onou5H28Wvy3kWnjxxdKQ</code>, then the collection <code class="language-plaintext highlighter-rouge">onou5H28Wvy3kWnjxxdKQ</code> must already exist in target instance, or there must be a YAML file with the export of a collection that has this ID.</p>
  </li>
</ul>

<div class="copy-clip-container h2"><h2 id="serialization-best-practices">Serialization best practices</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<div class="copy-clip-container h3"><h3 id="use-the-same-metabase-version-for-source-and-target-instance">Use the same Metabase version for source and target instance</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Currently, serialization only works if source and target Metabase have the same major version.
If you are using the CLI serialization commands, the version of the .jar file that you are using to run the serialization commands should match both the source and target Metabase versions as well.</p>

<div class="copy-clip-container h3"><h3 id="if-youre-using-h2-as-your-application-database-youll-need-to-stop-metabase-before-importing-or-exporting">If you’re using H2 as your application database, you’ll need to stop Metabase before importing or exporting</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>If you’re using Postgres or MySQL as your application database, you can import and export while your Metabase is still running.</p>

<div class="copy-clip-container h3"><h3 id="avoid-using-serialization-for-backups">Avoid using serialization for backups</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Just a note: serialization is <em>not</em> meant to back up your Metabase.</p>

<p>See <a href="./backing-up-metabase-application-data">Backing up Metabase</a>.</p>

<p>If you’re instead looking to do a one-time migration from the default H2 database included with Metabase to a MySQL/Postgres, then use the <a href="./migrating-from-h2">migration guide instead</a>.</p>

<div class="copy-clip-container h3"><h3 id="youll-need-to-manually-add-license-tokens">You’ll need to manually add license tokens</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Metabase excludes your license token from exports, so if you’re running multiple environments of Metabase Enterprise Edition, you’ll need to manually add your license token to the target Metabase(s), either via the <a href="/docs/latest/paid-features/activating-the-enterprise-edition">Metabase user interface</a>, or via an <a href="../configuring-metabase/environment-variables#mb_premium_embedding_token">environment variable</a>.</p>

<div class="copy-clip-container h3"><h3 id="metabase-adds-logs-to-exports-and-imports">Metabase adds logs to exports and imports</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Exports: Metabase adds logs to the compressed directory as <code class="language-plaintext highlighter-rouge">export.log</code>.</p>

<p>Imports: You can add the <code class="language-plaintext highlighter-rouge">-o -</code> flag to export logs directly into the terminal, or <code class="language-plaintext highlighter-rouge">-o import.log</code> to save to a file.</p>

<div class="copy-clip-container h2"><h2 id="serialization-with-cli-commands">Serialization with CLI commands</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<blockquote>
  <p>To serialize data on Metabase Cloud, use the <a href="#serialization-via-the-api">import and export API endpoints</a></p>
</blockquote>

<p>Metabase provides <a href="#exporting-with-cli"><code class="language-plaintext highlighter-rouge">export</code></a> and <a href="#importing-with-cli"><code class="language-plaintext highlighter-rouge">import</code></a> CLI commands.</p>

<p>See <a href="#how-export-works">How export works</a>, <a href="#how-import-works">How import works</a>, and <a href="#serialization-best-practices">Serialization best practices</a> for general information about serialization.</p>

<div class="copy-clip-container h3"><h3 id="exporting-with-cli">Exporting with CLI</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>To export the contents of a Metabase instance, change into the directory where you’re running the Metabase JAR and run:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar export dir_name
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>Where <code class="language-plaintext highlighter-rouge">dir_name</code> can be whatever you want to call the directory.</p>

<div class="copy-clip-container h3"><h3 id="export-options"><code class="language-plaintext highlighter-rouge">export</code> options</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>To view a list of <code class="language-plaintext highlighter-rouge">export</code> options, use the <code class="language-plaintext highlighter-rouge">help</code> command:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar help export
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>Which will run and then print something like:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">export path &amp; options
	 Serialize Metabase instance into directory at `path`.
	 Options:
	   -c, --collection ID             Export only specified ID; may occur multiple times.
	   -C, --no-collections            Do not export any content in collections.
	   -S, --no-settings               Do not export settings.yaml
	   -D, --no-data-model             Do not export any data model entities; useful for subsequent exports.
	   -f, --include-field-values      Include field values along with field metadata.
	   -s, --include-database-secrets  Include database connection details (in plain text; use caution).
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<h4 id="--collection"><code class="language-plaintext highlighter-rouge">--collection</code></h4>

<p>By default, Metabase will include all collections (except for personal collections) in the export. To include personal collections, you must explicitly add them with the <code class="language-plaintext highlighter-rouge">--collection</code> flag.</p>

<p>The <code class="language-plaintext highlighter-rouge">--collection</code> flag (alias <code class="language-plaintext highlighter-rouge">-c</code>) lets you specify by ID one or more collections to include in the export. You can find the collection ID in the collection’s URL, e.g., for a collection at: <code class="language-plaintext highlighter-rouge">your-metabase.com/collection/42-terraforming-progress</code>, the ID would be <code class="language-plaintext highlighter-rouge">42</code>.</p>

<p>If you want to specify multiple collections, separate the IDs with commas. E.g.,</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar export export_name --collection 1,2,3
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<h4 id="--no-collections"><code class="language-plaintext highlighter-rouge">--no-collections</code></h4>

<p>The <code class="language-plaintext highlighter-rouge">--no-collections</code> flag (alias <code class="language-plaintext highlighter-rouge">-C</code>) tells Metabase to exclude all collections from the export.</p>

<h4 id="--no-settings"><code class="language-plaintext highlighter-rouge">--no-settings</code></h4>

<p>The <code class="language-plaintext highlighter-rouge">--no-settings</code> flag (alias <code class="language-plaintext highlighter-rouge">-S</code>) tells Metabase to exclude the <code class="language-plaintext highlighter-rouge">settings.yaml</code> file that includes <a href="#general-metabase-settings-that-are-exported">site-wide settings</a>, which is exported by default.</p>

<h4 id="--no-data-model"><code class="language-plaintext highlighter-rouge">--no-data-model</code></h4>

<p>The <code class="language-plaintext highlighter-rouge">--no-data-model</code> flag (alias <code class="language-plaintext highlighter-rouge">-D</code>) tells Metabase to exclude the Table Metadata settings from the export. Admins define the metadata settings in the <a href="../data-modeling/metadata-editing">Table Metadata</a> tab of the Admin settings.</p>

<h4 id="--include-field-values"><code class="language-plaintext highlighter-rouge">--include-field-values</code></h4>

<p>The <code class="language-plaintext highlighter-rouge">--include-field-values</code> flag (alias <code class="language-plaintext highlighter-rouge">-f</code>) tells Metabase to include the sample values for field values, which Metabase uses to present dropdown menus. By default, Metabase excludes these sample field values.</p>

<h4 id="--include-database-secrets"><code class="language-plaintext highlighter-rouge">--include-database-secrets</code></h4>

<p>The <code class="language-plaintext highlighter-rouge">--include-database-secrets</code> flag (alias <code class="language-plaintext highlighter-rouge">-s</code>) tells Metabase to include connection details, including the database user name and password. By default, Metabase excludes these database connection secrets. If you don’t use this flag, you’ll need to manually input the credentials in the target Metabase.</p>

<div class="copy-clip-container h3"><h3 id="importing-with-cli">Importing with CLI</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>To import exported artifacts into a Metabase instance, go to the directory where you’re running your target Metabase (the Metabase you want to import into) and use the following command, where <code class="language-plaintext highlighter-rouge">path_to_export</code> is the path to the export that you want to import:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar import path_to_export
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>Currently, you can only import exported artifacts into a Metabase instance that was created from the same version of Metabase.</p>

<div class="copy-clip-container h3"><h3 id="import-options"><code class="language-plaintext highlighter-rouge">import</code> options</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Most options are defined when exporting data from a Metabase. To view a list of import flags, run:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar help import
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>Which prints out:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">import path &amp; options
         Load serialized Metabase instance as created by the [[export]] command from directory `path`.
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h2"><h2 id="serialization-via-the-api">Serialization via the API</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<blockquote>
  <p>Just like the CLI serialization commands, these endpoints are only available for <a href="/product/pro">Pro</a> and <a href="/product/enterprise">Enterprise</a> plans.</p>
</blockquote>

<p>You can import and export serialized Metabase data via Metabase’s API, which makes serialization possible for <a href="/cloud/">Metabase Cloud</a> deployments.</p>

<p>There are two endpoints:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">POST /api/ee/serialization/export</code></li>
  <li><code class="language-plaintext highlighter-rouge">POST /api/ee/serialization/import</code></li>
</ul>

<blockquote>
  <p>We use <code class="language-plaintext highlighter-rouge">POST</code>, not <code class="language-plaintext highlighter-rouge">GET</code>, for the <code class="language-plaintext highlighter-rouge">/export</code> endpoint. The export operation does not modify your Metabase, but it’s long and intensive, so we use <code class="language-plaintext highlighter-rouge">POST</code> to prevent accidental exports.</p>
</blockquote>

<p>For now, these endpoints are synchronous. If the serialization process takes too long, the request can time out. In this case, we suggest using the CLI commands.</p>

<p>See <a href="#how-export-works">How export works</a>, <a href="#how-import-works">How import works</a>, and <a href="#serialization-best-practices">Serialization best practices</a> for general information about serialization.</p>

<div class="copy-clip-container h3"><h3 id="api-export-parameters">API export parameters</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>You can append optional parameters to tell Metabase what to include or exclude from the export. You can also combine parameters (excluding, of course, <code class="language-plaintext highlighter-rouge">all_collections</code> and selective collections).</p>

<p>So, assuming you’re testing on <code class="language-plaintext highlighter-rouge">localhost</code>, and you want to exclude all collections from the export, you’d format the URL like so:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">http://localhost:3000/api/ee/serialization/export?all_collections=false
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>You can include multiple parameters, separated by <code class="language-plaintext highlighter-rouge">&amp;</code>. For example, to exclude both the settings and the data model from the export:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">http://localhost:3000/api/ee/serialization/export?data_model=false&amp;settings=false
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="collection"><code class="language-plaintext highlighter-rouge">collection</code></h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Type: Array of integers.</p>

<p>Default value: Metabase will export all collections, unless <code class="language-plaintext highlighter-rouge">all_collections</code> is set to <code class="language-plaintext highlighter-rouge">false</code>.</p>

<p>To select which collections to export, include the collection IDs. For example, to include collections <code class="language-plaintext highlighter-rouge">1</code> and <code class="language-plaintext highlighter-rouge">2</code>:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-html hljs language-xml" data-highlighted="yes">collection=1&amp;collection=2
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="all_collections"><code class="language-plaintext highlighter-rouge">all_collections</code></h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Type: Boolean</p>

<p>Default: <code class="language-plaintext highlighter-rouge">true</code> (unless you specify a subset of collections with <code class="language-plaintext highlighter-rouge">collection</code>).</p>

<p>To exclude all collections:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-html hljs language-xml" data-highlighted="yes">all_collections=false
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="settings"><code class="language-plaintext highlighter-rouge">settings</code></h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Type: Boolean.</p>

<p>Default: <code class="language-plaintext highlighter-rouge">true</code>.</p>

<p>To exclude the <code class="language-plaintext highlighter-rouge">settings.yaml</code> file that contains site-wide settings:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-html hljs language-xml" data-highlighted="yes">settings=false
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="data_model"><code class="language-plaintext highlighter-rouge">data_model</code></h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Type: Boolean.</p>

<p>Default: <code class="language-plaintext highlighter-rouge">true</code>.</p>

<p>To exclude the <a href="../data-modeling/metadata-editing">Table Metadata</a>:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">data_model=false
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="field_values"><code class="language-plaintext highlighter-rouge">field_values</code></h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Type: Boolean.</p>

<p>Default: <code class="language-plaintext highlighter-rouge">false</code>.</p>

<p>To include the sample values for field values, which Metabase uses to present dropdown menus:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">field_values=true
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="database_secrets"><code class="language-plaintext highlighter-rouge">database_secrets</code></h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Type: Boolean.</p>

<p>Default: <code class="language-plaintext highlighter-rouge">false</code>.</p>

<p>To include database connection details, like the database username and password:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="language-html hljs language-xml" data-highlighted="yes">database_secrets=true
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="dirname"><code class="language-plaintext highlighter-rouge">dirname</code></h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Type: String.</p>

<p>Default: <code class="language-plaintext highlighter-rouge">&lt;instance-name&gt;-&lt;YYYY-MM-dd_HH_mm&gt;</code></p>

<p>To specify a different directory:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">dirname=name_of_your_directory
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h3"><h3 id="you-must-compress-your-files-when-serializing-via-api-calls">You must compress your files when serializing via API calls</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>To keep file sizes over the network under control, both the <code class="language-plaintext highlighter-rouge">export</code> and <code class="language-plaintext highlighter-rouge">import</code> endpoints expect GZIP-compressed Tar files (<code class="language-plaintext highlighter-rouge">.tgz</code>).</p>

<h4 id="compress-a-directory">Compress a directory</h4>

<p>To compress a directory (e.g., a directory named <code class="language-plaintext highlighter-rouge">metabase_data</code>).</p>

<div class="language-sh highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight"><span class="nb">tar</span> <span class="nt">-czf</span>  metabase_data.tgz metabase_data
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<h4 id="extract-a-directory">Extract a directory</h4>

<p>To extract/unzip a directory:</p>

<div class="language-sh highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight"><span class="nb">tar</span> <span class="nt">-xvf</span>  metabase_data.tgz
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<div class="copy-clip-container h2"><h2 id="serialization-api-example">Serialization API example</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<div class="copy-clip-container h3"><h3 id="step-1-set-up-an-api-key">Step 1: Set up an API key</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<ol>
  <li>Create an <a href="../people-and-groups/api-keys">API key</a>.</li>
  <li>Assign the key to the Admin group</li>
</ol>

<div class="copy-clip-container h3"><h3 id="step-2-export">Step 2: Export</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<ol>
  <li>Send a <code class="language-plaintext highlighter-rouge">curl</code> request to export data:</li>
</ol>

<div class="language-sh highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">curl <span class="se">\</span>
  <span class="nt">-H</span> <span class="s1">'x-api-key: YOUR_API_KEY'</span> <span class="se">\</span>
  <span class="nt">-X</span> POST <span class="s1">'http://your-metabase-url/api/ee/serialization/export'</span> <span class="se">\</span>
  <span class="nt">-o</span> metabase_data.tgz
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>substituting <code class="language-plaintext highlighter-rouge">YOUR_API_KEY</code> with your API key and <code class="language-plaintext highlighter-rouge">your-metabase-url</code> with the URL of your Metabase instance.</p>

<blockquote>
  <p>We use <code class="language-plaintext highlighter-rouge">POST</code>, not <code class="language-plaintext highlighter-rouge">GET</code>, for the <code class="language-plaintext highlighter-rouge">/export</code> endpoint.</p>
</blockquote>

<p>This command will download the files as a GZIP-compressed Tar file named <code class="language-plaintext highlighter-rouge">metabase_data.tgz</code>.</p>

<ol>
  <li>Unzip the compressed file:</li>
</ol>

<div class="language-sh highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight"><span class="nb">tar</span> <span class="nt">-xvf</span> metabase_data.tgz
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>The extracted directory will be called something like <code class="language-plaintext highlighter-rouge">metabase-yyyy-MM-dd_HH-mm</code>, with the date and time of the export.</p>

<div class="copy-clip-container h3"><h3 id="step-3-import">Step 3: Import</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<ol>
  <li>Compress the directory containing serialized Metabase application data</li>
</ol>

<p>Let’s say you have your YAML files with Metabase application data in a directory called <code class="language-plaintext highlighter-rouge">metabase_data</code>. Before importing those files to your target Metabase, you’ll need to compress those files.</p>

<div class="language-sh highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight"><span class="nb">tar</span> <span class="nt">-czf</span> metabase_data.tgz metabase_data
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<ol>
  <li>POST to <code class="language-plaintext highlighter-rouge">/api/ee/serialization/import</code>.</li>
</ol>

<p>From the directory where you’ve stored your GZIP-compressed file, run:</p>

<div class="language-sh highlighter-rouge"><div class="highlight"><pre class="highlight"><div class="code-snippet-wrapper position-relative"><code class="no-highlight">curl <span class="nt">-X</span> POST <span class="se">\</span>
  <span class="nt">-H</span> <span class="s1">'x-api-key: YOUR_API_KEY'</span> <span class="se">\</span>
  <span class="nt">-F</span> <span class="nv">file</span><span class="o">=</span>@metabase_data.tgz <span class="se">\</span>
  <span class="s1">'http://your-metabase-url/api/ee/serialization/import'</span> <span class="se">\</span>
  <span class="nt">-o</span> -
</code><div class="copy-code-button">    <div class="copy-button-copy-wrapper d-flex align-items-center">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.5 15.25C5.5335 15.25 4.75 14.4665 4.75 13.5V6.75C4.75 5.64543 5.64543 4.75 6.75 4.75H13.5C14.4665 4.75 15.25 5.5335 15.25 6.5" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M17.25 8.75H10.75C9.64543 8.75 8.75 9.64543 8.75 10.75V17.25C8.75 18.3546 9.64543 19.25 10.75 19.25H17.25C18.3546 19.25 19.25 18.3546 19.25 17.25V10.75C19.25 9.64543 18.3546 8.75 17.25 8.75Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>        <p class="copy-button-copy">Copy</p>    </div>    <div class="copy-button-copied-wrapper align-items-center gap-1">        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.8897 6L21 7.09741L10.6165 19L4 11.9572L5.07138 10.8168L10.5761 16.6762L19.8897 6Z" fill="white"></path>
        </svg>        <p>Copied</p>    </div></div></div></pre></div></div>

<p>substituting <code class="language-plaintext highlighter-rouge">YOUR_API_KEY</code> with your API key and <code class="language-plaintext highlighter-rouge">your-metabase-url</code> with your Metabase instance URL.
The <code class="language-plaintext highlighter-rouge">-o -</code> option will output logs in the terminal.</p>

<blockquote>
  <p>If you import Metabase data into the same Metabase as you exported it from, you will overwrite your existing questions, dashboards, etc. See <a href="#how-import-works">How import works</a>.</p>
</blockquote>

<div class="copy-clip-container h2"><h2 id="other-uses-of-serialization">Other uses of serialization</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Serialization is intended for version control, staging-to-production workflows, and duplicating assets to other Metabase instances. While it’s possible to use serialization for other use cases (like duplicating assets <em>within</em> a single instance), we don’t officially support these use cases.</p>

<p>We’re providing some directions on how to approach these unsupported use cases, but you should use them at your own risk. We strongly recommend that you test any process involving serialization on a non-production instance first, and reach out to <a href="mailto:help@metabase.com">help@metabase.com</a> if you have any questions.</p>

<div class="copy-clip-container h3"><h3 id="using-serialization-for-duplicating-content-within-the-same-metabase">Using serialization for duplicating content within the same Metabase</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>Using serialization to duplicate content is not trivial, because you’ll need to wrangle <a href="#metabase-uses-entity-ids-to-identify-and-reference-metabase-items">Entity IDs</a> for all the items you want to duplicate — and the IDs for all the items that are related to those items — to avoid overwriting existing data.</p>

<p>Before starting this perilous journey, review <a href="#how-export-works">how export works</a> and <a href="#how-import-works">how import works</a>, and contact <a href="mailto:help@metabase.com">help@metabase.com</a> if you have any questions.</p>

<p>You’ll need to keep in mind:</p>

<ul>
  <li>Importing an item with an Entity ID that already exists will overwrite the existing item. To use an existing YAML file to create a new item, you’ll need to either a) create a new Entity ID or b) clear the Entity ID.</li>
  <li>Two items cannot have the same Entity IDs.</li>
  <li><code class="language-plaintext highlighter-rouge">entity_id</code> and <code class="language-plaintext highlighter-rouge">serdes/meta → id</code> fields in the YAML file should match.</li>
  <li>If the <code class="language-plaintext highlighter-rouge">entity_id</code> and <code class="language-plaintext highlighter-rouge">serdes/meta → id</code> fields in a YAML file for an item are blank, Metabase will create a new item with a new Entity ID.</li>
  <li>
    <p>All items and data sources referenced by an item should either already exist in target Metabase or be included in the import.</p>

    <p>For example, a collection can contain a dashboard that contains a question that is built on a model that references a data source. All of those dependencies must be either included in the import or already exist in the target instance.</p>

    <p>This means that you might need a multi-stage export/import: create some of the items you need (like collections) in Metabase first, export them to get their Entity IDs, then export the stuff that you want to duplicate and use those IDs in items that reference them.</p>
  </li>
</ul>

<p>For example, to duplicate a collection that contains <em>only</em> questions that are built directly on raw data (not on models or other saved questions), without changing the data source for the questions, you can use a process like this:</p>

<ol>
  <li>In Metabase, create a “template” collection and add the items you’d like to duplicate.</li>
  <li>In Metabase, create a new collection which will serve as the target for duplicated items.</li>
  <li>Export the template collection and the target collection (you can use <a href="#customize-what-gets-exported">export parameters</a> to export only a few collections).
The YAML files for template questions in the export will have their own Entity IDs and reference the Entity ID of the template collection.</li>
  <li>Get the Entity ID of the target collection from its export.</li>
  <li>
    <p>In the YAML files for questions in the template collection export:</p>

    <ul>
      <li>Clear the values for the fields <code class="language-plaintext highlighter-rouge">entity_id</code> and <code class="language-plaintext highlighter-rouge">serdes/meta → id</code> for questions. This will ensure that the template questions don’t get overwritten, and instead Metabase will create new questions.</li>
      <li>Replace <code class="language-plaintext highlighter-rouge">collection_id</code> references to the template collection with the ID of the new collection</li>
    </ul>
  </li>
  <li>Import the edited files.</li>
</ol>

<p>This process assumes that your duplicated questions will all use the same data source. You can combine this with <a href="#using-serialization-to-swap-the-data-source-for-questions-within-one-instance">switching the data source</a> to use a different data source for every duplicated collection.</p>

<p>If you want to create multiple copies of a collection at once, then instead of repeating this process for every copy, you could create your own target Entity IDs (they can be any string that uses the <a href="https://github.com/ai/nanoid">NanoID format</a>), duplicate all the template YAML files, and replace template Entity IDs and any references to them with your created Entity IDs.</p>

<p>If your collections contains dashboards, models, and other items that can add dependencies, this process can become even more complicated – you need to handle every dependency. We strongly recommend that you first test your serialization on a non-production Metabase, and reach out to <a href="mailto:help@metabase.com">help@metabase.com</a> if you need any help.</p>

<div class="copy-clip-container h3"><h3 id="using-serialization-to-swap-the-data-source-for-questions-within-one-instance">Using serialization to swap the data source for questions within one instance</h3><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 8px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>If you want to change the data source for some of the questions in your Metabase — for example, just for questions in a single collection - you can serialize the questions manually, then edit the exported YAML files.</p>

<blockquote>
  <p>If you want to switch <em>every</em> question built on database A to use database B instead, and database B has exactly the same schema as database A, you don’t need to use serialization: you can just swap the connection string in <strong>Admin &gt; Databases</strong></p>
</blockquote>

<p>Your databases must have the same engine, and ideally they should have the same schema.</p>

<p>You’ll need to keep in mind:</p>

<ul>
  <li>Databases, tables and fields are <a href="#databases-schemas-tables-and-fields-are-identified-by-name">referred to in Metabase by name</a></li>
  <li>Database connection details are not exported by default. To export database connection details, you’ll need to <a href="#customize-what-gets-exported">specify this in export parameters</a>.</li>
  <li>Databases, tables and fields referenced by an item should either already exist in the target Metabase, or be included in the import.</li>
</ul>

<p>For example, if you want to switch all questions in the <code class="language-plaintext highlighter-rouge">Movie reviews</code> collection to use the <code class="language-plaintext highlighter-rouge">Romance</code> database instead of the <code class="language-plaintext highlighter-rouge">Horror</code> database, and <em>both databases have the same schema</em>, you could follow a process like this:</p>

<ol>
  <li>In Metabase, add a new database connection in <strong>Admin &gt; Databases</strong> and name it <code class="language-plaintext highlighter-rouge">Romance</code>.</li>
  <li>
    <p>Export the collection <code class="language-plaintext highlighter-rouge">Movie reviews</code>.</p>

    <p>You can tell Metabase to export a single collection, or you can export all the collections and just work with files in the folder for the <code class="language-plaintext highlighter-rouge">Movie reviews</code> collection</p>
  </li>
  <li>In the YAML files for items from this collection, replace all references to <code class="language-plaintext highlighter-rouge">Horror</code> database with references to <code class="language-plaintext highlighter-rouge">Romance</code></li>
  <li>Import the edited files.</li>
</ol>

<p>Importing will overwrite the original questions. If you’re looking to create new questions that use a different data source, you can combine this process with <a href="#using-serialization-for-duplicating-content-within-the-same-metabase">Using serialization for duplicating assets</a>.</p>

<p>This process assumes that your new data source has exactly the same schema. If the schema is different, then you will also need to replace all references to all tables and fields. This process can be complicated and error-prone, so we strongly recommend that you test your serialization on a non-production instance first, and reach out to <a href="mailto:help@metabase.com">help@metabase.com</a> if you need any help.</p>

<div class="copy-clip-container h2"><h2 id="migrating-from-the-old-serialization-commands">Migrating from the old serialization commands</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<p>If you’re upgrading from Metabase version 46.X or older, here’s what you need to know:</p>

<ul>
  <li>The <code class="language-plaintext highlighter-rouge">export</code> command replaces the <code class="language-plaintext highlighter-rouge">dump</code> command.</li>
  <li>The <code class="language-plaintext highlighter-rouge">import</code> command replace the <code class="language-plaintext highlighter-rouge">load</code> command.</li>
</ul>

<p>A few other changes to call out:</p>

<ul>
  <li>The exported YAML files have a slightly different structure:
    <ul>
      <li>Metabase will prefix each file with a 24-character Entity ID (like <code class="language-plaintext highlighter-rouge">IA96oUzmUbYfNFl0GzhRj_accounts_model.yaml</code>).
You can run a Metabase command to <a href="./commands#drop-entity-ids">drop Entity IDs</a> before exporting.</li>
      <li>The file tree is slightly different.</li>
    </ul>
  </li>
  <li>To serialize personal collections, you just need to include the personal collection IDs in the list of comma-separated IDs following the <code class="language-plaintext highlighter-rouge">-c</code> option (short for <code class="language-plaintext highlighter-rouge">--collection</code>).</li>
</ul>

<p>If you’ve written scripts to automate serialization, you’ll need to:</p>

<ul>
  <li>Reserialize your Metabase using the upgraded Metabase (which uses the new <code class="language-plaintext highlighter-rouge">export</code> and <code class="language-plaintext highlighter-rouge">import</code> commands). Note that serialization will only work if you export and import your Metabase using the same Metabase version.</li>
  <li>Update those scripts with the new commands. See the new <a href="#export-options">export options</a>.</li>
  <li>If your scripts do any post-processing of the exported YAML files, you may need to update your scripts to accommodate the slightly different directory and YAML file structures.</li>
</ul>

<div class="copy-clip-container h2"><h2 id="further-reading">Further reading</h2><a class="copy-clip position-relative d-flex justify-content-center ms-2 hover-pointer" title="Copy to clipboard" style="margin-bottom: 0px;">
                           <svg class="share-button" width="32" height="32" viewBox="0 0 32 32" fill="#C6C9D2" xmlns="http://www.w3.org/2000/svg">
                               <path fill-rule="evenodd" clip-rule="evenodd" d="M19.2939 9.17106C19.5246 8.93228 19.8004 8.74183 20.1054 8.61081C20.4104 8.47978 20.7385 8.41082 21.0704 8.40793C21.4024 8.40505 21.7316 8.4683 22.0388 8.59401C22.3461 8.71971 22.6252 8.90534 22.8599 9.14007C23.0947 9.3748 23.2803 9.65393 23.406 9.96117C23.5317 10.2684 23.595 10.5976 23.5921 10.9296C23.5892 11.2615 23.5202 11.5896 23.3892 11.8946C23.2582 12.1996 23.0677 12.4754 22.8289 12.7061L19.0789 16.4561C18.6101 16.9247 17.9744 17.188 17.3114 17.188C16.6485 17.188 16.0128 16.9247 15.5439 16.4561C15.3082 16.2284 14.9924 16.1024 14.6647 16.1052C14.3369 16.1081 14.0234 16.2395 13.7917 16.4713C13.5599 16.703 13.4284 17.0166 13.4256 17.3443C13.4228 17.6721 13.5487 17.9878 13.7764 18.2236C14.7141 19.1609 15.9856 19.6875 17.3114 19.6875C18.6373 19.6875 19.9088 19.1609 20.8464 18.2236L24.5964 14.4736C25.5072 13.5305 26.0112 12.2675 25.9998 10.9566C25.9884 9.64557 25.4626 8.39151 24.5355 7.46447C23.6085 6.53743 22.3544 6.01158 21.0434 6.00019C19.7325 5.9888 18.4695 6.49277 17.5264 7.40356L15.6514 9.27856C15.5321 9.39387 15.4368 9.5318 15.3713 9.6843C15.3058 9.83681 15.2713 10.0008 15.2699 10.1668C15.2684 10.3328 15.3001 10.4974 15.3629 10.651C15.4258 10.8046 15.5186 10.9442 15.6359 11.0616C15.7533 11.1789 15.8929 11.2717 16.0465 11.3346C16.2001 11.3974 16.3647 11.4291 16.5307 11.4276C16.6967 11.4262 16.8607 11.3917 17.0132 11.3262C17.1657 11.2607 17.3036 11.1654 17.4189 11.0461L19.2939 9.17106ZM13.0439 15.4211C13.5128 14.9524 14.1485 14.6891 14.8114 14.6891C15.4744 14.6891 16.1101 14.9524 16.5789 15.4211C16.6942 15.5404 16.8322 15.6357 16.9847 15.7012C17.1372 15.7667 17.3012 15.8012 17.4672 15.8026C17.6332 15.8041 17.7978 15.7724 17.9514 15.7096C18.105 15.6467 18.2446 15.5539 18.3619 15.4366C18.4793 15.3192 18.5721 15.1796 18.635 15.026C18.6978 14.8724 18.7294 14.7078 18.728 14.5418C18.7266 14.3758 18.6921 14.2118 18.6266 14.0593C18.5611 13.9068 18.4658 13.7689 18.3464 13.6536C17.4088 12.7162 16.1373 12.1896 14.8114 12.1896C13.4856 12.1896 12.2141 12.7162 11.2764 13.6536L7.52644 17.4036C7.04889 17.8648 6.66798 18.4165 6.40593 19.0265C6.14389 19.6366 6.00596 20.2927 6.00019 20.9566C5.99442 21.6205 6.12093 22.2788 6.37233 22.8933C6.62374 23.5078 6.995 24.0661 7.46447 24.5355C7.93393 25.005 8.49219 25.3763 9.10667 25.6277C9.72115 25.8791 10.3796 26.0056 11.0434 25.9998C11.7073 25.994 12.3634 25.8561 12.9735 25.5941C13.5835 25.332 14.1352 24.9511 14.5964 24.4736L16.4714 22.5986C16.5908 22.4833 16.6861 22.3453 16.7516 22.1928C16.8171 22.0403 16.8516 21.8763 16.853 21.7103C16.8544 21.5443 16.8228 21.3797 16.76 21.2261C16.6971 21.0725 16.6043 20.9329 16.4869 20.8156C16.3696 20.6982 16.23 20.6054 16.0764 20.5425C15.9228 20.4797 15.7582 20.4481 15.5922 20.4495C15.4262 20.4509 15.2622 20.4854 15.1097 20.5509C14.9572 20.6164 14.8192 20.7117 14.7039 20.8311L12.8289 22.7061C12.5983 22.9448 12.3225 23.1353 12.0175 23.2663C11.7124 23.3973 11.3844 23.4663 11.0524 23.4692C10.7205 23.4721 10.3913 23.4088 10.0841 23.2831C9.77682 23.1574 9.49769 22.9718 9.26295 22.737C9.02822 22.5023 8.84259 22.2232 8.71689 21.9159C8.59118 21.6087 8.52793 21.2795 8.53082 20.9476C8.5337 20.6156 8.60267 20.2876 8.73369 19.9825C8.86471 19.6775 9.05517 19.4017 9.29394 19.1711L13.0439 15.4211Z"></path>
                           </svg> 
                            <div class="copy-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copy link to this section</div>
                            </div>
                            <div class="copied-to-clipboard-wrapper visible invisible">
                                <div class="caret"></div>
                                <div class="copied-to-clipboard">Copied to clipboard</div>
                            </div>
                        </a></div>

<ul>
  <li><a href="/learn/metabase-basics/administration/administration-and-operation/serialization">Serialization tutorial</a>.</li>
  <li><a href="/learn/metabase-basics/administration/administration-and-operation/multi-env">Multiple environments</a></li>
  <li><a href="/learn/metabase-basics/administration/administration-and-operation/git-based-workflow">Setting up a git-based workflow</a>.</li>
  <li>Need help? Contact <a href="mailto:support@metabase.com">support@metabase.com</a>.</li>
</ul>


        <div>
          <div class="widget-separator"></div>
          
            <p>
              Read docs for other <a href="/docs/all">versions of Metabase</a>.
            </p>
          
        </div>
      </div>