package com.skygreen.SkyGreen.Util;

public class JwtUtil {

    public static final String[] ENDPOINTS_WITH_USER_CAN_ACCESS = {
            "/auth/login",
            "/usuario/personal/**"
    };

    public static final String[] ENDPOINTS_WITH_ADMIN_CAN_ACCESS = {
            "/auth/register",    
            "/usuario/**",
            "/estoquevenda/**"
    };

    public static final String[] ENDPOINTS_WITH_GERENTE_CAN_ACCESS = {
            "/compras/**", 
            "/sementes/**", 
            "/fornecedor/**",
            "/producao/**", 
            "/estoque/**", 
            "/estoquevenda/**", 
            "/prateleira/**",
            "/cliente/**",
            "/vendas/**"
        };
        
        public static final String[] ENDPOINTS_WITH_ASSISTENTE_CAN_ACCESS = {
                "/compras/**", 
                "/sementes/**", 
                "/fornecedor/**",
                "/producao/**", 
                "/estoque/**", 
                "/estoquevenda/**", 
                "/prateleira/**",
                "/cliente/**",
                "/vendas/**"
    };
}
