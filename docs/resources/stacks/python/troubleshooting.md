# Troubleshooting

This section provides troubleshooting guidance for common issues encountered when deploying or running Python services on DataOS. Use these tips to quickly diagnose and resolve problems related to startup, dependencies, repository access, ingress, and performance.

## Pod does not start (CrashLoopBackOff)

When the Service keeps restarting and never becomes Ready.

Common causes & fixes:

- Git repository authentication failed → Verify credentials, secret, and syncFlags.

- baseDir incorrect → Ensure `baseDir` exists and contains `main.py` and `requirements.txt`.

- Repository not found → Ensure the correct repository URL and base URL are provided in the Service manifest file.
    
    ```bash
    dataos-ctl resource log -t service -w public -n python-service-sample            
    INFO[0000] 📃 log(public)...                             
    INFO[0001] 📃 log(public)...complete                     
    
                          NODE NAME                 │           CONTAINER NAME     ERROR  
    ────────────────────────────────────────────────┼────────────────────────────┼────────
      python-service-sample-7hw3-d-76b8664476-4ptgp │   python-service-sample    │        
    
    -------------------LOGS-------------------
    /etc/dataos/work
    --: 5: cd: can't cd to queries/pystack/app
    ```
    

## Dependency installation fails

When `pip install` breaks during startup.

Fixes:

- Verify package versions support Python 3.12
- Use specific package versions known to work; consult project docs

## Cannot access private repository

When the app cannot pull code from a private GitHub/Bitbucket repo.

Fixes:

- Check the repository username and token validity and permissions
- Ensure correct repo URL format (HTTPS)
- Include required git-sync flags
    
    ```bash
      stackSpec:
        repo:
          baseDir: queries/app
          syncFlags:
            - '--ref=main'
          url: https://bitbucket.org/queries/
    ```
    

## Ingress not working

When your app runs but cannot be accessed externally.

Checks:

- Port in manifest matches the app's listening port
- Ingress path configured correctly
- Authentication settings align with expectations (noAuthentication)

## Performance issues

When the app runs but consumes excessive CPU or memory.

Fixes:

- Increase resources or optimize code
- Use persistent volumes for intermediate data

## Getting help

If issues persist beyond these steps, escalate appropriately. Review logs and errors carefully, or contact your DataOS operator for cluster or networking issues.