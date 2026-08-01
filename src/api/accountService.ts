import api from "./axios";

export interface AccountSecurityRequest {
  username: string;
  current_password: string;
  new_password: string;
  confirm_password: string;
}

export const updateAccountSecurity = async (
  data: AccountSecurityRequest
) => {
  try {
    const response = await api.put(
      "users/account/update/",
      data
    );

    return response.data;

  } catch (error: any) {
    throw error;
  }
};